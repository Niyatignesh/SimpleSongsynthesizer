from scipy.io.wavfile import write
from numpy import linspace,sin,pi,int16,concatenate
from matplotlib import pylab
from pylab import plot,show,axis

# tone synthesis
def note(freq, len, amp=1, rate=44100):
 t = linspace(0,len,len*rate)
 data = sin(2*pi*freq*t)*amp
 return data.astype(int16) # two byte integers

# A tone, 2 seconds, 44100 samples per second
tone = note(440,1,amp=5000)
write('AsimpleSinewave.wav',44100,tone) # writing the sound to a file
plot(linspace(0,1,1*44100),tone)
axis([0,0.002,15000,-15000])
show()