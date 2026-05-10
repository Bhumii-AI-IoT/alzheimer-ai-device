# simulate_signals.py
# --------------------
# Simulates EEG brainwave signals and eye-tracking data for the
# Artificial Intelligence Enabled Device to Predict Alzheimer's Disease.
#
# In a real deployment this would be replaced by actual sensor data
# from hardware. This simulation is used for testing and development.
#
# Author: Bhumii-AI-IoT
# GitHub: https://github.com/Bhumii-AI-IoT

import numpy as np
import pandas as pd
import os

# ── Settings ──────────────────────────────────────────────────────────────────

SAMPLING_RATE_EEG = 256       # Hz - standard EEG sampling rate
SAMPLING_RATE_EYE = 60        # Hz - eye tracker frame rate
DURATION_SECONDS  = 30        # seconds per session
RANDOM_SEED       = 42        # makes results reproducible

np.random.seed(RANDOM_SEED)

# ── EEG Signal Simulation ─────────────────────────────────────────────────────

def simulate_eeg_signal(duration=DURATION_SECONDS, fs=SAMPLING_RATE_EEG, condition="healthy"):

    # Create time axis
    t = np.linspace(0, duration, duration * fs)

    # Alzheimer's brain has more slow waves and fewer fast waves
    if condition == "healthy":
        delta_amp = 0.5
        theta_amp = 0.8
        alpha_amp = 2.5   # strong alpha in healthy brain
        beta_amp  = 1.8
    else:
        delta_amp = 2.0   # elevated slow waves in Alzheimer's
        theta_amp = 2.2
        alpha_amp = 0.6   # reduced fast waves
        beta_amp  = 0.4

    # Build signal from frequency bands
    delta = delta_amp * np.sin(2 * np.pi * 2 * t)     # 2 Hz
    theta = theta_amp * np.sin(2 * np.pi * 6 * t)     # 6 Hz
    alpha = alpha_amp * np.sin(2 * np.pi * 10 * t)    # 10 Hz
    beta  = beta_amp  * np.sin(2 * np.pi * 20 * t)    # 20 Hz

    # Add noise to make it realistic
    noise = np.random.normal(0, 0.3, len(t))

    eeg_signal = delta + theta + alpha + beta + noise

    return eeg_signal, t


# ── Eye-Tracking Simulation ───────────────────────────────────────────────────

def simulate_eye_tracking(duration=DURATION_SECONDS, fs=SAMPLING_RATE_EYE, condition="healthy"):

    n_samples = duration * fs
    t = np.linspace(0, duration, n_samples)

    if condition == "healthy":
        # Healthy - precise gaze, fast saccades, normal blink rate
        gaze_x           = np.sin(2 * np.pi * 0.3 * t) + np.random.normal(0, 0.05, n_samples)
        gaze_y           = np.cos(2 * np.pi * 0.2 * t) + np.random.normal(0, 0.05, n_samples)
        saccade_velocity = np.abs(np.diff(gaze_x, prepend=gaze_x[0])) * fs
        blink_rate       = 0.25    # roughly 15 blinks per minute
    else:
        # Alzheimer's - erratic gaze, slower saccades, fewer blinks
        gaze_x           = np.sin(2 * np.pi * 0.1 * t) + np.random.normal(0, 0.3, n_samples)
        gaze_y           = np.cos(2 * np.pi * 0.1 * t) + np.random.normal(0, 0.3, n_samples)
        saccade_velocity = np.abs(np.diff(gaze_x, prepend=gaze_x[0])) * fs * 0.4
        blink_rate       = 0.08    # roughly 5 blinks per minute

    blink_events = (np.random.rand(n_samples) < blink_rate / fs).astype(int)

    df = pd.DataFrame({
        "time_s"           : t,
        "gaze_x"           : gaze_x,
        "gaze_y"           : gaze_y,
        "saccade_velocity" : saccade_velocity,
        "blink"            : blink_events
    })

    return df


# ── Generate Dataset ──────────────────────────────────────────────────────────

def generate_dataset(n_subjects=50, output_dir="data/simulated"):

    os.makedirs(output_dir, exist_ok=True)

    eeg_records  = []
    eye_records  = []
    labels       = []

    for i in range(n_subjects):

        condition = "alzheimers" if i % 2 == 0 else "healthy"
        label     = 1 if condition == "alzheimers" else 0

        # EEG summary features
        eeg_signal, _ = simulate_eeg_signal(condition=condition)
        eeg_records.append({
            "subject_id" : i,
            "condition"  : condition,
            "eeg_mean"   : np.mean(eeg_signal),
            "eeg_std"    : np.std(eeg_signal),
            "eeg_max"    : np.max(eeg_signal),
            "eeg_min"    : np.min(eeg_signal)
        })

        # Eye-tracking summary features
        eye_df = simulate_eye_tracking(condition=condition)
        eye_records.append({
            "subject_id"            : i,
            "condition"             : condition,
            "mean_saccade_velocity" : eye_df["saccade_velocity"].mean(),
            "blink_count"           : eye_df["blink"].sum(),
            "gaze_x_std"            : eye_df["gaze_x"].std(),
            "gaze_y_std"            : eye_df["gaze_y"].std()
        })

        labels.append({
            "subject_id" : i,
            "label"      : label,
            "condition"  : condition
        })

    pd.DataFrame(eeg_records).to_csv(f"{output_dir}/eeg_data.csv", index=False)
    pd.DataFrame(eye_records).to_csv(f"{output_dir}/eye_tracking_data.csv", index=False)
    pd.DataFrame(labels).to_csv(f"{output_dir}/labels.csv", index=False)

    print(f"Dataset saved to {output_dir}/")
    print(f"  - eeg_data.csv")
    print(f"  - eye_tracking_data.csv")
    print(f"  - labels.csv")


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    print("Alzheimer's AI Device - Signal Simulator")
    print("-" * 45)

    print("\nSimulating EEG - healthy subject...")
    eeg_h, _ = simulate_eeg_signal(condition="healthy")
    print(f"  Mean: {eeg_h.mean():.4f} | Std: {eeg_h.std():.4f}")

    print("\nSimulating EEG - Alzheimer's subject...")
    eeg_a, _ = simulate_eeg_signal(condition="alzheimers")
    print(f"  Mean: {eeg_a.mean():.4f} | Std: {eeg_a.std():.4f}")

    print("\nSimulating eye-tracking - healthy subject...")
    eye_h = simulate_eye_tracking(condition="healthy")
    print(f"  Blinks: {eye_h['blink'].sum()} | Mean saccade velocity: {eye_h['saccade_velocity'].mean():.4f}")

    print("\nSimulating eye-tracking - Alzheimer's subject...")
    eye_a = simulate_eye_tracking(condition="alzheimers")
    print(f"  Blinks: {eye_a['blink'].sum()} | Mean saccade velocity: {eye_a['saccade_velocity'].mean():.4f}")

    print("\nGenerating full dataset...")
    generate_dataset(n_subjects=100)