from pylab import *
from rtlsdr import *
from time import sleep
import matplotlib.pyplot as mp
sdr = RtlSdr()    
sdr.sample_rate = 2.4e6
sdr.center_freq = 93.5e6
sdr.gain = 4    

try:
    while True: # run until interrupted
        samples = sdr.read_samples(256*1024)
        mp.clf()
        mp.psd(samples.real, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
        mp.xlabel('Frequency (MHz)')
        mp.ylabel('Relative power (dB)')
        #mp.show()
        sleep(1) # sleep for 1s
except:
    pass

sdr.close()