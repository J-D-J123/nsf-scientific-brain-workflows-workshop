###
# Name: Joseph Johnson
# Date: 8/7/2026
#
# AI tool: Sonnet 5 Medium
# Percentage of code AI: 100%
#
# Description: Simulates downloading a dataset in 10 chunks from a research
# repository, with randomly injected network failures and automatic retries
# using exponential backoff, and logs the outcome of every attempt.
###

"""
Reliable Data Download Simulation
----------------------------------
Goal: model what a robust download pipeline looks like when pulling a large
research dataset over a network connection that isn't perfectly stable.

Why retry instead of just failing immediately?
A single dropped connection or a momentary server hiccup does NOT mean the
data is unavailable — it usually means "try again in a moment." If a script
gives up on the first error, you'd have to babysit every download and
manually restart it, which doesn't scale to large datasets with many chunks
or many files. Automatically retrying (with a growing wait between attempts,
called "exponential backoff") gives temporary problems time to resolve
themselves, while still eventually giving up if something is truly broken.
"""

import random
import time

# ---------------------------------------------------------------------------
# STEP 1: Simulate a single chunk download attempt
# ---------------------------------------------------------------------------
def download_chunk(chunk_id, failure_rate=0.4):
    """
    Simulates requesting one chunk of data from a research repository.

    In a real system, this function would make an HTTP request (e.g. with
    the `requests` library) to fetch a piece of a dataset. Here, we simulate
    that network call with a random chance of failure, standing in for
    things like dropped connections, timeouts, or the server being
    temporarily overloaded.

    Returns True if the "download" succeeded, False if it failed.
    """
    # random.random() gives a number between 0 and 1. If it's below our
    # failure_rate, we treat this attempt as a failed network request.
    if random.random() < failure_rate:
        return False
    return True


# ---------------------------------------------------------------------------
# STEP 2: Download one chunk, retrying with exponential backoff on failure
# ---------------------------------------------------------------------------
def download_with_retries(chunk_id, max_retries=5):
    """
    Attempts to download a single chunk, retrying on failure with an
    increasing wait time between attempts: 1s, 2s, 4s, 8s, 16s, ...

    This "exponential backoff" pattern is standard practice for network
    requests because:
      - A short wait after the first failure handles brief, one-off hiccups
        quickly without wasting much time.
      - Progressively longer waits after repeated failures avoid hammering
        an already-struggling server with rapid repeat requests, which
        could make the problem worse.
      - It still gives up after a reasonable number of attempts (max_retries)
        instead of retrying forever, in case something is genuinely broken.
    """
    attempt = 0

    while attempt <= max_retries:
        success = download_chunk(chunk_id)

        if success:
            # Report how many retries (attempts beyond the first) were needed
            print(f"  Chunk {chunk_id}: SUCCESS after {attempt} retr{'y' if attempt == 1 else 'ies'}")
            return True, attempt

        attempt += 1

        if attempt > max_retries:
            # We've used up all our allowed attempts — stop trying and
            # report this chunk as a real failure, not just a hiccup.
            print(f"  Chunk {chunk_id}: FAILED permanently after {max_retries} retries")
            return False, attempt - 1

        # Exponential backoff: wait longer after each successive failure.
        # 1s after the 1st failure, 2s after the 2nd, 4s after the 3rd, etc.
        wait_time = 2 ** (attempt - 1)
        print(f"  Chunk {chunk_id}: attempt {attempt} failed, retrying in {wait_time}s...")
        time.sleep(wait_time)


# ---------------------------------------------------------------------------
# STEP 3: Download all chunks in the dataset, one at a time
# ---------------------------------------------------------------------------
def download_dataset(n_chunks=10):
    """
    Downloads all chunks of a dataset sequentially, using the retry logic
    above for each one, and keeps a log of the outcome for every chunk.
    """
    results = []  # will hold (chunk_id, success, retries_needed) for each chunk

    print(f"Starting download of {n_chunks} chunks...\n")

    for chunk_id in range(1, n_chunks + 1):
        print(f"Requesting chunk {chunk_id}/{n_chunks}...")
        success, retries_needed = download_with_retries(chunk_id)
        results.append((chunk_id, success, retries_needed))
        print()  # blank line between chunks for readability

    return results


# ---------------------------------------------------------------------------
# STEP 4: Print a clear summary log of the whole download session
# ---------------------------------------------------------------------------
def print_summary(results):
    print("=" * 50)
    print("DOWNLOAD SUMMARY")
    print("=" * 50)

    succeeded = [r for r in results if r[1]]
    failed = [r for r in results if not r[1]]

    for chunk_id, success, retries in results:
        status = "SUCCESS" if success else "FAILED"
        print(f"  Chunk {chunk_id:2d}: {status:8s}  (retries needed: {retries})")

    print("-" * 50)
    print(f"Total chunks: {len(results)}")
    print(f"Succeeded: {len(succeeded)}")
    print(f"Failed permanently: {len(failed)}")

    if succeeded:
        avg_retries = sum(r[2] for r in succeeded) / len(succeeded)
        print(f"Average retries per successful chunk: {avg_retries:.1f}")


# ---------------------------------------------------------------------------
# Run the simulation
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    random.seed()  # uses system randomness; remove/set a fixed seed for reproducible test runs
    download_results = download_dataset(n_chunks=10)
    print_summary(download_results)