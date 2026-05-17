# preprocessing.py
# Author: Bhumii-AI-IoT
# Project: Artificial Intelligence Enabled Device to Predict Alzheimer's Disease
# Description: Takes raw simulated EEG and eye-tracking signals and prepares
#              them for feature extraction and machine learning.

import numpy as np
import pandas as pd
from scipy.signal import butter, filtfilt

# ── Settings ──────────────────────────────────────────────────────────────────

SAMPLING_RATE_EEG = 256    # Hz - must match simulate_signals.py
SAMPLING_RATE_EYE = 60     # Hz - must match simulate_signals.py

# ── EEG Preprocessing ─────────────────────────────────────────────────────────

def bandpass_filter(signal, lowcut, highcut, fs, order=4):
    # Butterworth bandpass filter
    # Removes frequencies outside the range we care about
    nyq = fs / 2
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    filtered = filtfilt(b, a, signal)
    return filtered


def preprocess_eeg(eeg_signal, fs=SAMPLING_RATE_EEG):
    # Step 1: Remove baseline drift using a high-pass filter
    # Anything below 0.5 Hz is noise, not brain activity
    highpass = bandpass_filter(eeg_signal, lowcut=0.5, highcut=50.0, fs=fs)

    # Step 2: Extract individual frequency bands
    # Each band corresponds to different types of brain activity
    delta = bandpass_filter(highpass, lowcut=0.5, highcut=4.0, fs=fs)   # slow waves
    theta = bandpass_filter(highpass, lowcut=4.0, highcut=8.0, fs=fs)   # memory related
    alpha = bandpass_filter(highpass, lowcut=8.0, highcut=13.0, fs=fs)  # relaxed awareness
    beta  = bandpass_filter(highpass, lowcut=13.0, highcut=30.0, fs=fs) # active thinking

    # Step 3: Calculate power in each band
    # Power = mean of squared signal values
    # In Alzheimer's: delta/theta power increases, alpha/beta power decreases
    band_powers = {
        'delta_power': np.mean(delta ** 2),
        'theta_power': np.mean(theta ** 2),
        'alpha_power': np.mean(alpha ** 2),
        'beta_power' : np.mean(beta ** 2)
    }

    return band_powers


# ── Eye-Tracking Preprocessing ────────────────────────────────────────────────

def preprocess_eye_tracking(eye_df):
    # Step 1: Remove outliers from gaze data
    # Readings beyond 3 standard deviations are likely noise or blinks
    gaze_x_clean = eye_df['gaze_x'].copy()
    gaze_y_clean = eye_df['gaze_y'].copy()

    x_mean, x_std = gaze_x_clean.mean(), gaze_x_clean.std()
    y_mean, y_std = gaze_y_clean.mean(), gaze_y_clean.std()

    gaze_x_clean = gaze_x_clean.clip(x_mean - 3*x_std, x_mean + 3*x_std)
    gaze_y_clean = gaze_y_clean.clip(y_mean - 3*y_std, y_mean + 3*y_std)

    # Step 2: Calculate clean saccade velocity
    saccade_velocity = np.abs(np.diff(gaze_x_clean, prepend=gaze_x_clean.iloc[0]))

    # Step 3: Extract summary statistics
    eye_features = {
        'mean_saccade_velocity' : saccade_velocity.mean(),
        'max_saccade_velocity'  : saccade_velocity.max(),
        'gaze_stability_x'      : gaze_x_clean.std(),
        'gaze_stability_y'      : gaze_y_clean.std(),
        'blink_count'           : eye_df['blink'].sum()
    }

    return eye_features


# ── Run ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":

    import sys
    sys.path.insert(0, '.')
    from src.data_collection.simulate_signals import simulate_eeg_signal, simulate_eye_tracking

    print("Alzheimer's AI Device - Preprocessing Pipeline")
    print("-" * 50)

    print("\nHealthy subject:")
    eeg_h, _ = simulate_eeg_signal(condition="healthy")
    eeg_features_h = preprocess_eeg(eeg_h)
    for key, value in eeg_features_h.items():
        print(f"  {key}: {value:.6f}")

    eye_h = simulate_eye_tracking(condition="healthy")
    eye_features_h = preprocess_eye_tracking(eye_h)
    for key, value in eye_features_h.items():
        print(f"  {key}: {value:.4f}")

    print("\nAlzheimer's subject:")
    eeg_a, _ = simulate_eeg_signal(condition="alzheimers")
    eeg_features_a = preprocess_eeg(eeg_a)
    for key, value in eeg_features_a.items():
        print(f"  {key}: {value:.6f}")

    eye_a = simulate_eye_tracking(condition="alzheimers")
    eye_features_a = preprocess_eye_tracking(eye_a)
    for key, value in eye_features_a.items():
        print(f"  {key}: {value:.4f}")

    print("\nPreprocessing complete.")