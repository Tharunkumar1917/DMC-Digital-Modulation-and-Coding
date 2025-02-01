# DMC-Digital-Modulation-and-Coding-
## FLAT TOP SAMPLING

The objective of this experiment is to study the process of Flat-Top Sampling ,
The experiment demonstrates how a continuous-time modulating signal (e.g., a sine wave) can be sampled using a flat-top approach 

### ALGORITHM

- Generate Modulating Signal: Create a sine wave with a specific frequency. This signal will serve as the base for the modulation.

- Generate Carrier Signal: Create a square wave (carrier signal) that will help in modulating the amplitude of the modulating signal.

- Sampling Process: Sample the modulating signal at specific time intervals (sampling rate), producing discrete samples.

- Flat-Top Sampling: For each sample, hold the sample value constant for a small duration (pulse_width), creating a "flat-top" appearance.

- Generate PAM Signal: Construct a PAM signal where each sample is represented by a rectangular pulse with amplitude corresponding to the sample value, with each pulse lasting for a specific time interval (pulse_width).

- Plot Results: Display the input sine wave, carrier square wave, flat-top sampled signal, and PAM signal. 

### Code Explanation:

- fs (Sampling Frequency): Defines how often the continuous signal is sampled per second.
- T (Sampling Interval): The time interval between two consecutive samples.
- modulating_signal: A sine wave that modulates the PAM signal.
- carrier_signal: A square wave that serves as the carrier for the modulation.
- sampling_times: The time points where samples of the modulating signal are taken.
- Plotting: The code uses matplotlib to display the results.


###  Input Values

- Sampling frequency (fs): 100 Hz
- Modulating signal frequency (f_signal): 5 Hz (sine wave)
- Carrier signal frequency (f_carrier): 20 Hz (square wave)

 ### OUTPUT

 ![image](https://github.com/user-attachments/assets/9e1ed2a5-c15b-48d9-8ba6-c2441749e68d)

  ### Conclusion

Flat-Top Sampling is an effective method of discretizing a continuous-time signal by holding each sampled value constant for a finite duration. 
This results in a series of rectangular pulses, where the amplitude of each pulse corresponds to the sampled value of the modulating signal. 
While this method introduces some distortion compared to ideal sampling (which uses impulse functions), 
it provides a practical approach to signal representation, especially in communication systems. 
The duration of each pulse (pulse width) is a key factor in determining the quality and accuracy of the sampled signal, 
and it must be carefully chosen to balance the trade-off between time resolution and signal fidelity.


