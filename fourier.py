from tkinter.filedialog import askopenfilename
from scipy.fftpack import fft
from scipy.io import wavfile
from matplotlib import pyplot as plt

filename = askopenfilename(filetypes=(("Audio Files", ".wav"), ("All Files", "*.*")))
fs, data = wavfile.read(filename)
first_channel = data.T[0]
fourier = fft(first_channel)
fourier_length = len(fourier)
fourier = fourier[:(fourier_length // 2)]
plt.plot(abs(fourier), 'r')
plt.show()