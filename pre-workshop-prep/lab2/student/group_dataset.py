###
# Name: Joseph Johnson
# Date: 8/7/2026
#
# AI tool: Sonnet 5 Medium
# Percentage of AI code: 100%
#
# Description: Simulates loading and combining neural recording data (64
# channels x 1000 timepoints x 3 conditions) from 50 research participants
# into a single group-level array using NumPy, reports memory usage, and
# projects memory needs for a 500-participant study.
###

"""
Simulating and Combining Multi-Participant Neuroscience Data
--------------------------------------------------------------
Goal: scale up from analyzing one participant's data to a full group-level
dataset of 50 participants, using NumPy efficiently.

Each participant's raw data is shaped like a typical EEG/neural recording:
    64 channels  x  1000 time points  x  3 experimental conditions
(e.g. 64 electrodes, 1000 samples per trial, 3 task conditions)
"""

import numpy as np

# ---------------------------------------------------------------------------
# STEP 1: Simulate loading data for each of 50 participants
# ---------------------------------------------------------------------------
# In a real study, this loop would call something like `load_participant(id)`
# to read each person's file from disk. Here we simulate that with random
# data standing in for recorded neural signals (e.g. microvolts of EEG).

n_participants = 50
n_channels = 64        # number of recording electrodes/channels
n_timepoints = 1000     # number of time samples recorded per trial
n_conditions = 3        # number of experimental conditions

# We collect each participant's array in a plain Python list first.
# This is normal and fine — the "unnecessary copies" issue we need to avoid
# comes in the COMBINING step, not the collection step.
participant_arrays = []

for participant_id in range(n_participants):
    # Simulate one participant's dataset: random values standing in for
    # real recorded brain signals, shaped (channels, timepoints, conditions).
    # We use float32 instead of the NumPy default float64 to cut memory
    # usage in half — a common practical choice for large neural datasets.
    participant_data = np.random.randn(n_channels, n_timepoints, n_conditions).astype(np.float32)
    participant_arrays.append(participant_data)

print(f"Simulated data for {n_participants} participants.")
print(f"Each participant's array shape: {participant_arrays[0].shape}  "
      f"(channels, timepoints, conditions)")

# ---------------------------------------------------------------------------
# STEP 2: Combine all participants into a single group-level array
# ---------------------------------------------------------------------------
# Naively calling np.concatenate or np.vstack repeatedly inside a loop is
# inefficient: each call allocates a brand-new, slightly bigger array and
# copies all the old data into it — resulting in dozens of large temporary
# copies for 50 participants.
#
# The efficient approach: pre-allocate the final array ONCE at the correct
# full size, then fill in each participant's slice directly. This avoids
# ever creating in-between "growing" copies of the data.

group_data = np.empty((n_participants, n_channels, n_timepoints, n_conditions), dtype=np.float32)

for i, participant_data in enumerate(participant_arrays):
    group_data[i] = participant_data  # writes directly into pre-allocated memory, no copy of the whole array

# Alternative one-liner that achieves the same result just as efficiently,
# since np.stack on a list of same-shaped arrays performs a single
# allocation internally:
#   group_data = np.stack(participant_arrays, axis=0)

# ---------------------------------------------------------------------------
# STEP 3: Report size, shape, and memory usage of the combined dataset
# ---------------------------------------------------------------------------
print("\n--- Group-level dataset summary ---")
print(f"Shape: {group_data.shape}  "
      f"(participants, channels, timepoints, conditions)")

# .nbytes gives the exact amount of memory (in bytes) the array occupies in RAM
bytes_used = group_data.nbytes
mb_used = bytes_used / (1024 ** 2)
gb_used = bytes_used / (1024 ** 3)

print(f"Total elements: {group_data.size:,}")
print(f"Memory used: {bytes_used:,} bytes  "
      f"({mb_used:.2f} MB / {gb_used:.4f} GB)")

# ---------------------------------------------------------------------------
# STEP 4: Estimate memory usage if the study scaled to 500 participants
# ---------------------------------------------------------------------------
# Memory scales linearly with participant count, since every participant
# contributes an identical-sized block of data. So we can estimate the
# 500-participant case just by scaling up the per-participant memory cost,
# without actually generating that much data (which could be several GB).

n_participants_scaled = 500
bytes_per_participant = bytes_used / n_participants
estimated_bytes_scaled = bytes_per_participant * n_participants_scaled
estimated_gb_scaled = estimated_bytes_scaled / (1024 ** 3)

print(f"\n--- Projected memory usage for {n_participants_scaled} participants ---")
print(f"Estimated total size: {estimated_bytes_scaled:,.0f} bytes "
      f"(~{estimated_gb_scaled:.2f} GB)")

if estimated_gb_scaled > 8:
    print("Note: this exceeds typical laptop RAM (8-16GB) — at this scale, "
          "you'd likely want to process participants in batches, use "
          "memory-mapped arrays (np.memmap), or downsample/compress the data "
          "rather than loading everything into memory at once.")