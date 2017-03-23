from scipy.io.wavfile import write
from numpy import linspace,sin,pi,int16,concatenate
from matplotlib import pylab
from pylab import plot,show,axis

# tone synthesis
def note(freq, len, amp=1, rate=44100):
 t = linspace(0,len,len*rate)
 data = sin(2*pi*freq*t)*amp
 return data.astype(int16) # two byte integers

# A number of tones   44100 samples per second amplitude =5000
t1 = note(185,0.2,amp=5000)
t2=note(196,0.2,amp=5000)
t3=note(220,0.4,amp=5000)
t4=note(220,0.4,amp=5000)
t5=note(247,0.4,amp=5000)
t6=note(247,0.4,amp=5000)
t7=note(220,0.6,amp=5000)
t8=note(196,0.2,amp=5000)
t9=note(185,0.4,amp=5000)
t10=note(277,0.4,amp=5000)
t11=note(294,0.8,amp=5000)
t12=note(330,0.4,amp=5000)
t13=note(277,0.2,amp=5000)
t14=note(294,0.4,amp=5000)
t15=note(220,0.8,amp=5000)

#Song notes in sequence: (F0 Hz, Duration ms)
#(185,200) (196,200) (220,400) (220,400) (247,400) (247,400) (220,600) (196, 200) (185, 400)
at1=concatenate((t1,t2,t3,t4,t5,t6,t7,t8,t9),axis=1)
#(185,200) (196,200) (220,400) (220,400) (247,400) (247,400) (220,600) (196, 200) (185, 400)
at2=concatenate((at1,at1),axis=1)
#185,200) (196,200) (220,400) (220,400) (247,400) (277,400) (294,800);
at3=concatenate((t1,t2,t3,t4,t5,t10,t11),axis=1)
#(294,400)  (330,400) (277,400) (277,400) (247,400) (277,200) (247,400) (220,800)
at4=concatenate((t14,t12,t10,t10,t6,t13,t5,t15),axis=1)

#combining HUM HONGE KAMIYAB
tone4=concatenate((at2,at3,at4),axis=1)


write('song1.wav',44100,tone4) # writing the sound to a file


plot(linspace(0,12.6,12.6*44100),tone4)
axis([0,1,15000,-15000])
show()