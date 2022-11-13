from pylab import *
from rtlsdr import *
import matplotlib.pyplot as mp
sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.4e6
sdr.center_freq = 103e6
sdr.gain = 4

samples = sdr.read_samples(256*1024)
sdr.close()
#print(+samples)

# use matplotlib to estimate and plot the PSD
lines = mp.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
mp.xlabel('Frequency (MHz)')
mp.ylabel('Relative power (dB)')
lines.get_data()
mp.show()
