import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt

rate, data = wavfile.read("output.wav")
t = np.arange(len(data[:, 0]))*1.0/rate
# plt.plot(t, data[:, 0])
# plt.show()

p = 20*np.log10(np.abs(np.fft.rfft(data[:2048, 0])))
f = np.linspace(0, rate/2.0, len(p))
plt.plot(f, p)
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude(dB)")
plt.show()
