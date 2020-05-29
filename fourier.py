from scipy.fftpack import fft
from scipy.io import wavfile
from matplotlib import pyplot as plt


def calculate_fourier(file_name):
    fs, data = wavfile.read(file_name)
    first_channel = data.T[0]
    fourier = fft(first_channel)
    fourier_length = len(fourier)
    fourier = fourier[:(fourier_length // 2)]
    plt.plot(abs(fourier), 'r')
    plt.show()
