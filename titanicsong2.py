from scipy.io.wavfile import write
from numpy import linspace,sin,pi,int16,concatenate
from matplotlib import pylab
from pylab import plot,show,axis

# tone synthesis
def note(freq, len, amp=1, rate=44100):
 t = linspace(0,len,len*rate)
 data = sin(2*pi*freq*t)*amp
 return data.astype(int16) # two byte integers

# A tone 44100 samples per second
t1 = note(262,0.2,amp=5000)
t2=note(294,0.2,amp=5000)
t3=note(330,1,amp=5000)
t4=note(262,0.8,amp=5000)
t5=note(294,0.4,amp=5000)
t6=note(392,0.8,amp=5000)
t7=note(349.23,0.2,amp=5000)
t8=note(330,0.2,amp=5000)
t9=note(220,0.8,amp=5000)
t10=note(196,1.2,amp=5000)
t11=note(292,0.2,amp=5000)
t12=note(440,0.8,amp=5000)
t13=note(294,1.6,amp=5000)
t14=note(262,0.6,amp=5000)
t15=note(262,0.4,amp=5000)
t16=note(247,0.4,amp=5000)
t17=note(330,0.8,amp=5000)
t18=note(294,0.8,amp=5000)
t19=note(196,3.2,amp=5000)
t20=note(262,1.6,amp=5000)
t21=note(294,1.2,amp=5000)
t22=note(196,0.4,amp=5000)
t23=note(349.23,0.4,amp=5000)
t24=note(330,0.4,amp=5000)
t25=note(330,1.2,amp=5000)
t26=note(220,1.6,amp=5000)
t27=note(196,1.6,amp=5000)

#Song notes in sequence: (F0 Hz, Duration ms)
#(262,200), (294,200), (294,200), (330,1000), (294,200), (262,200), (294,400), (392,800), (349.23,200), (330,200), (262,800), (220, 800), (196, 1200); 
at1=concatenate((t1,t2,t2,t3,t2,t1,t5,t6,t7,t8,t4,t9,t10),axis=1)
#(262,200), (294,200), (294,200), (330,1000), (294,200), (262,200), (294,400), (392,800), (330,200), (392,200), (440,800), (392,800), (294,1600);
at2=concatenate((t1,t2,t2,t3,t2,t1,t5,t6,t8,t11,t12,t6,t13),axis=1)

#(262,600), (262, 200), (262,400), (262,400), (247, 400), (262, 800), (262,400), (247,400), (262,800), (294,400), (330,800), (294,800), (262,600), (262, 200), (262,400), (262,400), (247, 400), (262, 800), (262,400), (196,3200);
at3=concatenate((t14,t1,t15,t15,t16,t4,t15,t16,t4,t5,t17,t18,t14,t1,t15,t15,t16,t4,t15,t19),axis=1)

#(262,600), (262, 200), (262,400), (262,400), (247, 400), (262, 800), (262,400), (247,400), (262,800), (294,400), (330,800), (294,800), (262,600), (262, 200), (262,400), (262,400), (247, 400), (262, 800), (262,400), (196,3200);
at4=concatenate((at3,at3),axis=1)

#(262,1600), (294,1200), (196,400), (392,800), (349.23,400), (330,400), (294,800), (330,400), (349.23,400), (330,1200), (294,200), (262,200), (247,400), (262,800), (247,400), (220,1600), (196,1600);
at5=concatenate((t20,t21,t22,t6,t23,t24,t18,t24,t23,t25,t2,t1,t16,t4,t16,t26,t27),axis=1)

#Combining all four and making it a TITNIC TONE
tone4=concatenate((at1,at2,at4,at5),axis=1)


write('song2.wav',44100,tone4) # writing the sound to a file


