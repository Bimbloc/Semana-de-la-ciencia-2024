# %%

import matplotlib.pyplot as plt
#import pyaudio
from scipy.io import wavfile
import numpy as np
import wave, sys
signal = 0
samplerate=0
samplerate ,signal = wavfile.read('output.wav')
samples  = signal.size
seconds = samples/samplerate
timestamps=[]
timestamps = [i for i in range(samples) ]

#plt.axis([0,100,0,4500])
#plt.plot(timestamps,signal,'bo')
plt.figure(figsize=(30, 15))
plt.axis([0,4200,30000,33500])
plt.rcParams['path.simplify'] = True
plt.rcParams['agg.path.chunksize'] = 850
plt.step(timestamps,signal)
    # shows the plot  
    # in new window 
plt.show() 
#se ve guay  por arriba pero molaria ver la onda entera 
   
bta = 2
# %%
import matplotlib.pyplot as plt
#import pyaudio
from scipy.io import wavfile
import numpy as np
import wave, sys
signal = 0
samplerate=0
samplerate ,signal = wavfile.read('output.wav')
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
plt.step(timestamps,signal)
    # shows the plot  
    # in new window 
plt.show() 
#se ve guay  por arriba pero molaria ver la onda entera 
   
# %%

import matplotlib.pyplot as plt
#import pyaudio
from scipy.io import wavfile
import numpy as np
import wave, sys
def visualize(path: str): 
    
    # reading the audio file 
    raw = wave.open(path) 
      
    # reads all the frames  
    # -1 indicates all or max frames 
    signal = raw.readframes(-1) 
    signal = np.frombuffer(signal, dtype ="int16") 
      
    # gets the frame rate 
    f_rate = raw.getframerate() 
  
    # to Plot the x-axis in seconds  
    # you need get the frame rate  
    # and divide by size of your signal 
    # to create a Time Vector  
    # spaced linearly with the size  
    # of the audio file 
    time = np.linspace( 
        0, # start 
        len(signal) / f_rate, 
        num = len(signal) 
    ) 
  
    # using matplotlib to plot 
    # creates a new figure 
    plt.figure(1) 
      
    # title of the plot 
    plt.title("Sound Wave") 
      
    # label of x-axis 
    plt.xlabel("Time") 
    # axis limits 
    plt.axis([0,10,-1000,4500]) 
    # actual plotting 
    #plt.plot(time, signal,'r+') 
    plt.rcParams['path.simplify'] = True
    plt.rcParams['agg.path.chunksize'] = 850
    
    plt.step(time,signal)
    # shows the plot  
    # in new window 
    plt.show() 
     # you can also save 
    # the plot using 
    # plt.savefig('filename') 
    # 
    # 
    
path = "output.wav"
visualize(path) 
#%%

# %%
