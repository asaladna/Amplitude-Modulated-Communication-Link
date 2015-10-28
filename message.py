import pylab as pl
import numpy as np
import scipy.io.wavfile as wav


def sin():
    sin_frequency = 400
    sample_freq = 8000
    t = pl.arange(0., 1., 1./sample_freq)
    msg = pl.sin(2*pl.pi*sin_frequency*t)
    msg = Message(sample_freq, t, msg)
    return msg


def square():
    square_frequency = 40
    sample_freq = 8000
    t = pl.arange(0., 1., 1./sample_freq)
    msg = pl.sign(pl.sin(2*pl.pi*square_frequency*t))  # sign rounds to -1 or 1
    msg = Message(sample_freq, t, msg)
    return msg


def pulse_train():
    pass


def voice():
    rate, data = wav.read('name.wav')
    data = data[:, 0]
    msg = Message(rate, np.arange(0., len(data)/rate, 1/rate), data)
    return msg


class Message():
    def __init__(self, sample_frequency, t, msg):
        self.fs = sample_frequency
        self.t = t
        self.msg = msg

    def write(self, filename='audio.wav'):
        wav.write(filename, self.fs, self.msg)