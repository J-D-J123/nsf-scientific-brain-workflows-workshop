###
# Name: Joseph Johnson
# Date: 8/7/2026
#
# AI tool: Sonnet 5 Medium
# Percentage of code AI: 100%
#
# Description: Simulates a multi-channel dataset with 100,000 time points,
# saves it as both a plain-text CSV and a binary NumPy (.npy) file, then
# compares file size on disk and load time back into memory.
###

"""
CSV vs. Binary (.npy): Choosing a Data Storage Format
---------------------------------------------------------
Goal: show concretely why the file format you choose to save research data
in matters — not just for how much disk space it uses, but for how fast
you can load it back for analysis later.

Two formats compared here:

  CSV (plain text): Every number is stored as human-readable text
  (e.g. "3.14159265"), separated by commas, with a newline per row.
  You can open it in Excel or a text editor and read it directly. But
  storing numbers as text is inefficient — the text form of a number
  usually takes up more bytes than the number itself needs in memory,
  and the computer has to re-parse (convert text back to numbers) every
  single value when loading it, which takes time.

  .npy (NumPy binary): Numbers are stored in the exact same raw binary
  form the computer uses when they're in memory (e.g. 4 or 8 bytes per
  number, no text conversion needed). This makes files smaller and much
  faster to load, at the cost of not being human-readable — you need
  NumPy (or a compatible tool) to open it, not a plain text editor.
"""

import numpy as np
import time
import os


# ---------------------------------------------------------------------------
# STEP 1: Simulate a multi-channel dataset
# ---------------------------------------------------------------------------
n_timepoints = 100_000
n_channels = 16  # e.g. 16 recording channels/electrodes

# Simulate measurement data: random values standing in for a real signal
# (e.g. voltage readings), shaped (timepoints, channels).
rng = np.random.default_rng(0)
data = rng.standard_normal((n_timepoints, n_channels)).astype(np.float64)

print(f"Simulated dataset shape: {data.shape} "
      f"({n_timepoints:,} time points x {n_channels} channels)")
print(f"Total values: {data.size:,}\n")


# ---------------------------------------------------------------------------
# STEP 2: Save the dataset in both formats
# ---------------------------------------------------------------------------
os.makedirs("output", exist_ok=True)
csv_path = "output/dataset.csv"
npy_path = "output/dataset.npy"

# --- Save as CSV (plain text) ---
# Every number gets converted to its text representation and written out
# with commas between values and a newline per row — the same format
# you'd see if you opened this in a spreadsheet program.
start = time.perf_counter()
np.savetxt(csv_path, data, delimiter=",")
csv_save_time = time.perf_counter() - start

# --- Save as .npy (binary) ---
# Numbers are written directly in their raw binary form, exactly as NumPy
# stores them in memory — no text conversion step needed.
start = time.perf_counter()
np.save(npy_path, data)
npy_save_time = time.perf_counter() - start

print(f"CSV save time:  {csv_save_time:.3f}s")
print(f"NPY save time:  {npy_save_time:.3f}s\n")


# ---------------------------------------------------------------------------
# STEP 3: Compare file sizes on disk
# ---------------------------------------------------------------------------
csv_size = os.path.getsize(csv_path)
npy_size = os.path.getsize(npy_path)

print("--- File size comparison ---")
print(f"CSV file size:  {csv_size:,} bytes  ({csv_size / (1024**2):.2f} MB)")
print(f"NPY file size:  {npy_size:,} bytes  ({npy_size / (1024**2):.2f} MB)")
print(f"CSV is {csv_size / npy_size:.2f}x larger than NPY on disk\n")
# CSV is larger because each number is stored as several text characters
# (e.g. "-1.23456789012345" is 18 characters/bytes) instead of a fixed
# 8 bytes for a float64 number in binary form.


# ---------------------------------------------------------------------------
# STEP 4: Compare load times back into memory
# ---------------------------------------------------------------------------
# --- Load from CSV ---
# This requires re-parsing every text value back into a number, which is
# much slower than just reading raw bytes.
start = time.perf_counter()
loaded_from_csv = np.loadtxt(csv_path, delimiter=",")
csv_load_time = time.perf_counter() - start

# --- Load from .npy ---
# The binary data is read essentially as-is into memory, with minimal
# extra processing required.
start = time.perf_counter()
loaded_from_npy = np.load(npy_path)
npy_load_time = time.perf_counter() - start

print("--- Load time comparison ---")
print(f"CSV load time:  {csv_load_time:.3f}s")
print(f"NPY load time:  {npy_load_time:.3f}s")
print(f"Loading from CSV took {csv_load_time / npy_load_time:.1f}x longer than NPY\n")

# Sanity check: confirm both loaded versions match the original data
assert np.allclose(loaded_from_csv, data), "CSV round-trip data mismatch!"
assert np.array_equal(loaded_from_npy, data), "NPY round-trip data mismatch!"
print("Both files loaded back correctly and match the original data.\n")


# ---------------------------------------------------------------------------
# When to use which format
# ---------------------------------------------------------------------------
print("--- When to choose each format ---")
print("CSV: use when you need the file to be human-readable, opened in "
      "Excel/Google Sheets, shared with non-programmers, or version-controlled "
      "as readable text (e.g. small config tables, summary results).")
print("NPY (or HDF5 for very large/complex datasets): use for large numeric "
      "datasets that only your own analysis code will read, where load speed "
      "and disk space matter more than human-readability — e.g. raw sensor "
      "or recording data feeding into a NumPy/Python analysis pipeline.")