import pyaudio
import wave
import time
import matplotlib.pyplot as plt
import numpy as np


class AudioRecorder:
    chunk = 4096
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100

    def record_audio(self, seconds=3):
        filename = time.strftime("%Y_%m_%d_%H_%M_%S") + ".wav"
        frames = []

        print('Output will be saved as: ' + filename)

        p = pyaudio.PyAudio()
        print('Recording...')

        stream = p.open(format=self.sample_format,
                        channels=self.channels,
                        rate=self.fs,
                        frames_per_buffer=self.chunk,
                        input=True)

        for i in range(0, int(self.fs / self.chunk * seconds)):
            data = stream.read(self.chunk)
            frames.append(data)

        stream.stop_stream()
        stream.close()
        p.terminate()

        print('Finished recording')

        wf = wave.open(filename, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.sample_format))
        wf.setframerate(self.fs)
        wf.writeframes(b''.join(frames))
        wf.close()

        return filename

    def generate_plot(self, filename):
        wf = wave.open(filename, 'r')

        speech = wf.readframes(-1)
        speech = np.fromstring(speech, "Int16")
        fs = wf.getframerate()

        time_range = np.linspace(0, len(speech) / fs, num=len(speech))

        plt.figure(1)
        plt.title("Speech from " + filename)
        plt.plot(time_range, speech)
        plt.ylabel("Amplitude")
        plt.xlabel("Time [s]")
        plt.show()

        wf.close()
