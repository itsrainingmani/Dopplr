import scipy.io.wavfile as wavfile
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

rate, data = wavfile.read("output.wav")
t = np.arange(len(data[:, 0]))*1.0/rate
# plt.plot(t, data[:, 0])
# plt.show()

# stride = int(round(1./rate)) # of sample in 1 second
window = signal.hamming(2048)
# window /= np.sqrt((window**2).sum() / rate)

# print type(data[:2048, 0]), len(data[:2048, 0])
# print data[0][0]

# p = 20*np.log10(np.abs(np.fft.rfft(data[:2048, 0])))
j = []
for i in xrange(2048):
	j.append(data[i][0]*window[i])
p = 20*np.log10(np.abs(np.fft.rfft(j)))
f = np.linspace(0, rate/2.0, len(p))

print len(p)

plt.plot(f, p)
plt.xlabel("Frequency(Hz)")
plt.ylabel("Amplitude(dB)")
plt.figure(1)
plt.show()