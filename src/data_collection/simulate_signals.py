"""
simulate_signals.py
--------------------
Simulates EEG brainwave signals and eye-tracking data for the
Artificial Intelligence Enabled Device to Predict Alzheimer's Disease.

In a real deployment, this module would be replaced by actual sensor
data from hardware. This simulation is used for pipeline development,
testing, and demonstrating the concept.

Author: Bhumii-AI-IoT
GitHub: https://github.com/Bhumii-AI-IoT
"""

import numpy as np
import pandas as pd
import os

# ── Settings ──────────────────────────────────────────────────────────────────

SAMPLING_RATE_EEG = 256       # Hz — standard EEG sampling rate
SAMPLING_RATE_EYE = 60        # Hz — eye tracker frame rate
DURATION_SECONDS  = 30        # Length of each simulated session
RANDOM_SEED       = 42        # Makes results reproducible

np.random.seed(RANDOM_SEED)

# ── EEG Signal Simulation ─────────────────────────────────────────────────────

def simulate_eeg_signal(duration=DURATION_SECONDS, fs=SAMPLING_RATE_EEG, condition="healthy"):
    """
    Simulate a single-channel EEG signal.

    In Alzheimer's, brainwave patterns change in a measurable way:
    - Slow waves (delta, theta) increase
    - Fast waves (alpha, beta) decrease

    Parameters:
        duration  : how many seconds of signal to generate
        fs        : sampling rate in Hz
        condition : 'healthy' or 'alzheimers'

    Returns:
        eeg_signal : the simulated signal as a numpy array
        t          : the time axis
    """

    t = np.linspace(0, duration, duration * fs)

    if condition == "healthy":
        # Healthy brain — strong alpha and beta activity
        delta_amp = 0.5
        theta_amp = 0.8
        alpha_amp = 2.5
        beta_amp  = 1.8
    else:
        # Alzheimer's brain — elevated slow waves, reduced fast waves
        delta_amp = 2.0
        theta_amp = 2.2
        alpha_amp = 0.6
        beta_amp  = 0.4

    # Build each frequency band as a sine wave
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
    """
    Simulate eye-tracking data.

    In Alzheimer's, eye movements change in measurable ways:
    - Saccades become slower and less accurate
    - Blink rate decreases
    - Gaze becomes less stable

    Parameters:
        duration  : how many seconds of data to generate
        fs        : eye tracker sampling rate in Hz
        condition : 'healthy' or