import numpy as np
import matplotlib.pyplot as plt

# Parameters
fs = 100                  # Sampling frequency
T = 1 / fs                # Sampling interval
pulse_width = 0.1 * T     # Width of PAM pulses (10% of T)
t = np.arange(0, 1, 0.001)  # High-resolution time vector for smooth plotting
f_signal = 5              # Frequency of the modulating signal (sine wave)
f_carrier = 20            # Frequency of the carrier signal (square wave)

# Modulating signal (sine wave)
modulating_signal = np.sin(2 * np.pi * f_signal * t)

# Carrier signal (square wave)
carrier_signal = 0.5 * (1 + np.sign(np.sin(2 * np.pi * f_carrier * t)))

# Sampling process
sampling_times = np.arange(0, 1, T)  # Time instants for sampling
sampled_values = np.sin(2 * np.pi * f_signal * sampling_times)  # Sampled values

# Create flat-top sampled signal
flat_top_signal = np.zeros_like(t)
for i in range(len(sampling_times) - 1):
    start_idx = int(sampling_times[i] / 0.001)  # Convert time to index
    end_idx = int(sampling_times[i + 1] / 0.001)
    flat_top_signal[start_idx:end_idx] = sampled_values[i]  # Hold the value constant

# Create PAM signal with finite-duration pulses
pam_signal = np.zeros_like(t)
for i in range(len(sampling_times)):
    start_time = sampling_times[i]
    end_time = start_time + pulse_width
    start_idx = int(start_time / 0.001)
    end_idx = int(end_time / 0.001)
    if end_idx > len(t):  # Avoid index overflow
        end_idx = len(t)
    pam_signal[start_idx:end_idx] = sampled_values[i]  # Set rectangular pulse

# Plotting
plt.figure(figsize=(12, 10))

# Input Sine Wave
plt.subplot(3, 1, 1)
plt.plot(t, modulating_signal, label='Input Sine Wave', color='blue')
plt.title('Input Sine Wave')

plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Square Wave (Carrier Signal)
plt.subplot(3, 1, 2)
plt.plot(t, carrier_signal, label='Square Wave (Carrier)', color='orange')
plt.title('Square Wave (Carrier Signal)')

plt.ylabel('Amplitude')
plt.grid()
plt.legend()

# Flat-Top Sampled Signal with Sine Wave Overlay
plt.subplot(3, 1, 3)
plt.step(t, flat_top_signal, label='Flat-Top Sampled Signal', color='red', where='post')
plt.plot(t, modulating_signal, label='Input Sine Wave', color='blue', linestyle='dashed')
plt.title('Flat-Top Sampled Signal ')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show() 

