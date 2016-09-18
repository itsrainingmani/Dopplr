from __future__ import division #Avoid division problems in Python 2
import math
import pyaudio
import sys

PyAudio = pyaudio.PyAudio
FREQ = float(input("Enter the required frequency - "))
RATE = 16000
# WAVE = 2109.89
speed_of_sound = 34500
WAVE = speed_of_sound/FREQ
print WAVE
data = ''.join([chr(int(math.sin(x/((RATE/WAVE)/math.pi))*127+128)) for x in xrange(RATE)])
p = PyAudio()

stream = p.open(format =
                p.get_format_from_width(1),
                channels = 1,
                rate = RATE,
                output = True)
for DISCARD in xrange(5):
    stream.write(data)
stream.stop_stream()
stream.close()
p.terminate()