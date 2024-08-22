import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
data1 = np.loadtxt('/content/sample_data/Data_1.txt')
data2 = np.loadtxt('/content/sample_data/Data_2.txt')
def find_and_plot_peaks(data, label):
    peaks, _ = find_peaks(data, distance=20, prominence=0.5)
    inversed_data = -data
    minima, _ = find_peaks(inversed_data, distance=20, prominence=0.5)

    plt.figure(figsize=(10, 6))
    plt.plot(data, label=f'{label} Signal', color='black')
    plt.plot(peaks, data[peaks], 'ro', label='Maxima')
    plt.plot(minima, data[minima], 'bo', label='Minima')
    plt.title(f'{label} Signal Peaks')
    plt.xlabel('Index')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.show()

find_and_plot_peaks(data1, 'Data_1')
find_and_plot_peaks(data2, 'Data_2')