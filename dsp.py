# -*- coding: utf-8 -*-
"""DSP

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1luA2dR8eXCBCJPYPp5DyDZp57Fnf4ifg

4. Record an audio and eliminate high frequency noises from it.
"""

import thinkdsp as nk
import thinkplot as plt
from IPython.display import Audio
wave=nk.read_make('C:/Users/aa/Downloads.wav')
spectrm=wave.make_spectrum()
spectrm.plot(low=2000)
s=Audio(data=wave.ys,rate=wave.framerate)
s

"""1. Create a mixture of 3 sinusoids of different linear frequencies which will be you date of birth."""

import numpy as np
import matplotlib.pyplot as plt


t1 = [np.sin(2*np.pi*t)*22 for t in np.linspace(0,1, 1000)]

t2 = [np.sin(5*np.pi*t)*6 for t in np.linspace(0,5, 1000)]

t3 = [np.sin(7*np.pi*t)*00 for t in np.linspace(0,4, 1000)]
S=[i+J+K for i,J,K in zip(t1,t2,t3)]



B=np.fft.fft(S)

plt.plot(abs(B[0]))
plt.plot(B)
plt.show()

"""Create a music of your choice and export the audio in .wav format."""

import thinkdsp as d
from IPython.display import Audio
w1=d.SinSignal(freq=240,amp=5,offset=0)
w2=d.SinSignal(freq=270,amp=5,offset=0)
w3=d.SinSignal(freq=300,amp=5,offset=0)
w4=d.SinSignal(freq=320,amp=5,offset=0)
w5=d.SinSignal(freq=360,amp=5,offset=0)
w6=d.SinSignal(freq=400,amp=5,offset=0)
w7=d.SinSignal(freq=450,amp=5,offset=0)


sa_time=w1.make_wave(duration=1.5,start=0,framerate=11000)
re_time=w2.make_wave(duration=1.5,start=1.5,framerate=11000)
ga_time=w3.make_wave(duration=1.5,start=3,framerate=11000)
ma_time=w4.make_wave(duration=1.5,start=4.5,framerate=11000)
pa_time=w5.make_wave(duration=1.5,start=6,framerate=11000)
dha_time=w6.make_wave(duration=1.5,start=7.5,framerate=11000)
ni_time=w7.make_wave(duration=1.5,start=9,framerate=11000)
ni_time=w7.make_wave(duration=1.5,start=9,framerate=11000)
dha_time=w6.make_wave(duration=1.5,start=7.5,framerate=11000)
#sa_time=w1.make_wave(duration=1.5,start=10.5,framerate=11000)
time=sa_time+re_time+ ga_time+ma_time+pa_time+dha_time+ni_time+sa_time
d=Audio(data=time.ys,rate=time.framerate)
d
