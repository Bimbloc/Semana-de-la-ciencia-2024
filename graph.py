
import matplotlib.pyplot as plt
#import pyaudio
from scipy.io import wavfile
from scipy.fftpack import fft
import numpy as np
import wave, sys
signal = 0
samplerate=0
#codificado en scottie 1 por que tenemos mucha informacion 
#https://radio.clubs.etsit.upm.es/blog/2019-08-10-sstv-scottie1-encoder/
samplerate ,signal = wavfile.read('scot1.wav')
samples  = signal.size
seconds = samples/samplerate
timestamps=[]
timestamps = [i for i in range(samples) ]

#plt.axis([0,100,0,4500])
#plt.plot(timestamps,signal,'bo')
plt.figure(figsize=(30, 15))
plt.axis([0,4200,-3400,3400])
plt.rcParams['path.simplify'] = True
plt.rcParams['agg.path.chunksize'] = 850
signal = signal/100
#poemos pintar de distintos colores las distintas partes de las señal
#header = signal[]
#plt.step(timestamps,signal)
#podemos dibujar la frecuencia y el tiempo 
#con el tiempo en segundos
plt.axis([0,100,-3400,3400])
#plt.plot(np.arange (len(signal))/samplerate,fft(signal))
fig,(st,sf) = plt.subplots(2,1,constrained_layout=1)
signalf = fft(signal)
sf.plot(np.abs(signalf[:samplerate//2]),lw=0.15)
sf.grid(1)

    # shows the plot  
    # in new window 
plt.show() 
#se ve guay  por arriba pero molaria ver la onda entera 