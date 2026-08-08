###
# Name: Joseph Johnson
# Date: 8/8/2026
#
# AI tool: Sonnet 5 Medium
# Percentage of code AI: 100%
#
# Description: Compares running a rolling-average analysis on 10 datasets
# one at a time versus in parallel across multiple CPU cores using
# multiprocessing, times both approaches, and charts the speedup.
###

"""
Sequential vs. Parallel Processing: A Performance Comparison
---------------------------------------------------------------
Goal: show, concretely, why analyzing multiple participants' data in
parallel (using multiple CPU cores) can be dramatically faster than
analyzing them one at a time on a single core — and by how much.

The core idea: a normal Python loop uses ONE CPU core, no matter how many
cores your computer has. If you have 10 independent datasets to analyze
(independent = analyzing one doesn't depend on the results of another),
you can hand each one to a different core and have them all crunch numbers
at the same time, instead of waiting for each one to finish before starting
the next.
"""

import time
import numpy as np
import multiprocessing as mp
import matplotlib
matplotlib.use("Agg")  # render to file instead of a GUI window
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------------
# STEP 1: Define a moderately demanding analysis function
# ---------------------------------------------------------------------------
def rolling_average(data, window=500):
    """
    Computes a rolling (moving) average across a large 1D array.

    This is a realistic stand-in for a common step in data analysis
    (e.g. smoothing a noisy signal). It's "moderately demanding" because
    it has to do a small amount of math at every one of many positions
    in a large array, which adds up to real computation time.
    """
    n = len(data)
    result = np.empty(n - window + 1)
    for i in range(len(result)):
        # Average of the values in the current sliding window.
        # Deliberately done with a Python loop (not the fast vectorized
        # NumPy way) so the function takes a noticeable amount of time —
        # standing in for a more complex real-world analysis step.
        result[i] = np.mean(data[i:i + window])
    return result


def analyze_one_dataset(dataset):
    """
    Wraps rolling_average() so it can be handed to either a normal loop
    or a multiprocessing worker in exactly the same way.
    """
    return rolling_average(dataset)


# ---------------------------------------------------------------------------
# STEP 2: Create 10 independent "participant" datasets
# ---------------------------------------------------------------------------
def make_datasets(n_datasets=10, size=20000, seed=0):
    rng = np.random.default_rng(seed)
    # Each dataset simulates one participant's recording: a long array of
    # noisy values (e.g. a continuous signal over time).
    return [rng.standard_normal(size) for _ in range(n_datasets)]


# ---------------------------------------------------------------------------
# STEP 3: Run the analysis one dataset at a time (sequential / single-core)
# ---------------------------------------------------------------------------
def run_sequential(datasets):
    """
    Processes each dataset one after another, using only a single CPU core.
    Even though your computer may have several cores, a plain Python loop
    like this never uses more than one of them — the other cores sit idle
    the whole time.
    """
    start = time.perf_counter()
    results = [analyze_one_dataset(d) for d in datasets]
    elapsed = time.perf_counter() - start
    return results, elapsed


# ---------------------------------------------------------------------------
# STEP 4: Run the analysis in parallel across multiple CPU cores
# ---------------------------------------------------------------------------
def run_parallel(datasets):
    """
    Distributes the 10 datasets across a "pool" of worker processes, one
    per available CPU core. Each core works on its own dataset(s)
    independently and at the same time, so the total time is roughly the
    time for ONE dataset, not ten, as long as you have enough cores.

    This works well here because the datasets are independent: analyzing
    participant 3 doesn't need any information from participant 7, so
    there's no reason they can't be computed simultaneously.
    """
    n_cores = mp.cpu_count()
    start = time.perf_counter()
    with mp.Pool(processes=n_cores) as pool:
        results = pool.map(analyze_one_dataset, datasets)
    elapsed = time.perf_counter() - start
    return results, elapsed, n_cores


# ---------------------------------------------------------------------------
# STEP 5: Compare the two approaches and chart the result
# ---------------------------------------------------------------------------
def main():
    datasets = make_datasets()
    print(f"Created {len(datasets)} datasets, each with {len(datasets[0]):,} data points.\n")

    print("Running SEQUENTIAL analysis (one dataset at a time, one core)...")
    _, sequential_time = run_sequential(datasets)
    print(f"  Sequential time: {sequential_time:.3f} seconds\n")

    print("Running PARALLEL analysis (multiple datasets at once, multiple cores)...")
    _, parallel_time, n_cores = run_parallel(datasets)
    print(f"  Detected {n_cores} CPU core(s) available.")
    print(f"  Parallel time: {parallel_time:.3f} seconds\n")

    speedup = sequential_time / parallel_time
    print(f"Speedup factor: {speedup:.2f}x")
    if n_cores == 1:
        print("Note: only 1 CPU core is available in this environment, so "
              "parallel processing has no extra cores to use — it may run "
              "about the same speed or even slightly slower here due to the "
              "overhead of starting worker processes. On a multi-core "
              "machine, the parallel version would be substantially faster.")

    # --- Bar chart comparing the two approaches ---
    fig, ax = plt.subplots(figsize=(6, 5))
    approaches = ["Sequential\n(1 core)", f"Parallel\n({n_cores} core{'s' if n_cores != 1 else ''})"]
    times = [sequential_time, parallel_time]
    colors = ["#4C72B0", "#55A868"]

    bars = ax.bar(approaches, times, color=colors)
    ax.set_ylabel("Time (seconds)")
    ax.set_title(f"Sequential vs. Parallel Processing\n(10 datasets, speedup: {speedup:.2f}x)")

    # Label each bar with its exact time for readability
    for bar, t in zip(bars, times):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(),
                 f"{t:.3f}s", ha="center", va="bottom")

    plt.tight_layout()
    plt.savefig("/mnt/user-data/outputs/sequential_vs_parallel.png", dpi=150)
    print("\nBar chart saved to sequential_vs_parallel.png")


if __name__ == "__main__":
    main()