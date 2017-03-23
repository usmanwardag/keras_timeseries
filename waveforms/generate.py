import numpy as np
import pickle

import scipy.signal as signal

"""
Generate a pickle file with 400 samples (with 
128 data points each) for the following 3 waveforms:

- Squre waveform
- Sawtooth waveform
- PWM waveform

Also add random guassian noise.
"""

def gen_waveform(t, freq, wave='square'):
	""" 
	Generate a waveform of specific frequency
	against the given timestamps.

	Arguments
	---------
	t: numpy array
		Time series to plot against

	freq: int
		Frequency of desired waveform

	wave: str
		Accepts 'square', 'sawtooth' or 'pwm'.
	"""

	if wave == 'square':
		return signal.square(2 * np.pi * freq * t)

	elif wave == 'sawtooth':
		return signal.sawtooth(2 * np.pi * freq * t)

	elif wave == 'pwm':
		signal.square(2 * np.pi * freq * t, duty=(sig + 1)/2)

def add_noise(sig):
	"""Adds random guassian noise to the signal. """

	noise = np.random.normal(0, 1, len(sig))
	return sig + 0.1*noise

def time_slice(sig, N=128, K=64):
	""" Time slice signal into samples of 128 data
	points. 

	Arguments
	---------
	sig: numpy array
		Input signal

	N: int
		Window length

	K: int
		Overlap between windows
	"""

	k = len(data) / K
	X = np.zeros((k, 1, N))

	low = 0
	high = N

	for i in range(0, k-1):
		X[i] = sig[low:high]
		low += K
		high += K

	return X


# 128*200 because we have an overlap of 50%
# (see time_slice function)
t = np.linspace(0, 1, 128 * 200, endpoint=False)

from matplotlib import pyplot as plt
data = gen_waveform(t, 1000, 'square')
data = add_noise(data)
data = time_slice(data)

#plt.plot(data[10][0])

plt.show()


