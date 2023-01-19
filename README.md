# RTL-SDR

With Regards Bishal Paudel ;) 

## A) You might be wondering, what is RTL-SDR?

Software-defined radio (SDR) is a radio communication system where components that have been traditionally implemented in hardware (e.g. mixers, filters, amplifiers, modulators/demodulators, detectors, etc.) are instead implemented by means of software on a personal computer, or another computer device (could be a Raspberry PI or a dedicated system). 

RTL-SDR (RealTek) is a low-cost USB device that can be used as a computer-based radio for receiving live radio signals. Depending on the RTL-SDR it could receive frequencies from 500 kHz up to 1.75 GHz.

## B) Objective of the project:

At higher frequencies(Ku-Ka band), the satellite signal starts degrading due to comparable size of rain droplets with the wavelength of the signal. To study the attenuation with respect to rainfall we require spectrum analyzers to process the signals. The average cost of spetcrum analyzer is very high hence it is not ideal to perform multi-site experiments causing a hinderance to study spatial distribution of signal degradation during rainfall.

With this project we aim to create a low cost solution for spectrum analyzer using RTL-SDR.

## C) Setup
As a cost effective replacement of Spectrum Analyzer for the reception of 11.17 GHz satellite signal was done using RTL Software Defined Radio(SDR). The RTL SDR was used in an Raspberry Pi to continuously monitor the signal to study the signal degradation in an multi-site arrangement.

GSAT-14 satellite signal is recieved using a dish antenna,LNB and set-top box. The recieved signal is of 11.17 GHz which is downconverted by **Low noise block(LNB)** to 1.42 GHz. Power stectral density of the signal from 1419 MHz to 1421 MHz is plotted keeping 1.42 GHz as a center frequency.

<p align="center">
<img width="600" alt="Screenshot_20230119_204828" src="https://user-images.githubusercontent.com/62088646/213483822-bc453d82-7b5e-4715-bfa2-5abd2cc29b42.jpeg">
</p>
The command in the picture rtl_power defines the parameters and feeds the signal data recieved from the satelite to the psd.py script to plot the power spectral density of the recieved signal.

## D) Site Pictures:
Below collage is some of the glimpses of testing and deployment of the device in outdoor. 
<p align="center">
<img width="600" alt="Screenshot_20230119_204828" src="https://user-images.githubusercontent.com/62088646/213488952-6562fa75-f3f3-44de-995e-2e0e8517dea0.jpg">
</p>






