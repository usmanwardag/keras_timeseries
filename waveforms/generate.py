import numpy as np
import pickle

import scipy.signal as signal

"""
Generate a pickle file with 100 samples (with 
128 data points each) for the following 3 waveforms:

- Squre waveform
- Sawtooth waveform
- Sinusoid

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
        Accepts 'square', 'sawtooth' or 'sin'.
    """

    if wave == 'square':
        return signal.square(2 * np.pi * freq * t)

    elif wave == 'sawtooth':
        return signal.sawtooth(2 * np.pi * freq * t)

    elif wave == 'sin':
        return np.sin(2 * np.pi * freq * t)

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

    k = len(sig) / K
    X = np.zeros((k, 1, N))

    low = 0
    high = N

    for i in range(0, k-1):
        X[i] = sig[low:high]
        low += K
        high += K

    return X

def create_dataset():
    """
    Main function to create dataset using the
    helper functions defined above.
    """

    dataset = {}
    sigs = ['square', 'sawtooth', 'sin']

    for sig in sigs:
        # 128*50 because we have an overlap of 50%
        # (see time_slice function)
        t = np.linspace(0, 1, 128 * 50, endpoint=False)

        data = gen_waveform(t, 100, sig)
        data = add_noise(data)   
        dataset[(sig)] =  time_slice(data)

        with open('dataset.pickle', 'wb') as handle:
            pickle.dump(dataset, handle)

    return dataset

create_dataset()

