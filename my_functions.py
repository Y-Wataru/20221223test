


from matplotlib import pyplot as plt
import numpy as np
plt.style.use('graphdesign.mplstyle')

def plot_fft(t, f, max_f, filename):
	# FFT
	
	N = t.shape[0]
	dt = t[1] - t[0]
	
	F = np.fft.fft(f)
	freq = np.fft.fftfreq(N, d=dt)
	
	plt.rcParams['figure.figsize'] = 16, 6
	fig1, ax1 = plt.subplots(1, 2)
	fig1.subplots_adjust(hspace=0.6, wspace=0.4)
	ax1[0].plot(t, f, linewidth=2, color='r')
	ax1[0].set_xlabel("Time delay [ps]")
	ax1[0].set_ylabel("Intensity [arb. unit]")
	
	ax1[1].plot(freq[1:int(N/2)], np.abs(F[1:int(N/2)]), linewidth=2, color='r')
	#ax1[1].set_yscale("linear")
	ax1[1].set_yscale("log")
	ax1[1].set_xlabel("Frequency [THz]")
	ax1[1].set_ylabel("FT intensity [arb. unit]")
	ax1[1].set_xlim([0, max_f])
	ax1[1].set_ylim([1, 300])
	fig1.savefig(filename)
	plt.show()


def FT_Filter(f, t, mode ,cut_freq):
	N = t.shape[0]
	dt = t[1] - t[0]
	
	F = np.fft.fft(f)
	freq = np.fft.fftfreq(N, d=dt)
	
	if mode == "hpf":
		filter = np.where(np.abs(freq) > cut_freq, 1, 0)
	elif mode == "lpf":
		filter = np.where(np.abs(freq) < cut_freq, 1, 0)
	
	F_HPF = F * filter
	
	f_ifft = np.fft.ifft(F_HPF)
	f_ifft = f_ifft.real
	
	return f_ifft

