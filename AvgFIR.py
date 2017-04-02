from pylab import *
import random 

#Standard low pass filter 

a=[]
b=[]

def calc(fc,fs):
	y = float(sqrt(2)/2)
	w = float(2*fc*pi/fs)
	n = 1
	while True:
		x = (sin(n*w/2)/sin(w/2))/n
		if x<y:
			return n
		n = n+1

def averageFilter(data, n):
    datos = []
    for item in data:
        datos.append(item)
    samples = []
    summ = 0
    res = []
    for i in range(n):
        samples.append(0)
    for i in range(len(datos)):
        x = samples.pop()
        samples.insert(0,datos.pop(0))
        summ = sum(samples)
        res.append(float(summ)/n)
    return res
    
def plotSpectrum(y,Fs):
    """
     Plots a Single-Sided Amplitude Spectrum of y(t)
    """
    n = len(y) # length of the signal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]
 
    plot(frq,abs(Y),'r') # plotting the spectrum
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')
    return
    

Fs = 100;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = arange(0,16,Ts) # time vector
#freq = 523.25
freq = 300
Fc = 5

a = 1 + sin(2*pi*(1.5 + t)*t) #chirp
#a = 1 + sin(2*pi*freq*t)

subplot(4,1,1)
plot(t,a)
xlabel('Time')
ylabel('Amplitude')
subplot(4,1,2)
plotSpectrum(a,Fs)
#savefig("Prueba3.png")

n = calc(Fc,Fs)
b = averageFilter(a, n) 

subplot(4,1,3)
plot(t,b)
xlabel('Time')
ylabel('Amplitude')
subplot(4,1,4)
plotSpectrum(b,Fs)
#savefig("Prueba4.png")
show()
