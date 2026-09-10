import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# 1. Učitavanje EKG signala
file_path = 'Audio and ECG-20260611T153310Z-3-001\\Audio and ECG\\Zmaj 2 stres\\opensignals_0007808CADDB_2024-12-10_19-43-05.txt'
data = pd.read_csv(file_path, sep='\t', comment='#', header=None)
ecg_signal = data.iloc[:, 2].values

# 2. Frekvencija uzorkovanja
fs = 1000  # Hz

# Vremenski vektor
time = np.arange(len(ecg_signal)) / fs

plt.figure(figsize=(15,5))
plt.plot(time, ecg_signal, color='steelblue')

plt.xlabel("Vrijeme [s]")
plt.ylabel("Amplituda [ADC]")
plt.title("Originalni EKG signal")
plt.grid(True)

plt.tight_layout()
plt.show()

# 3. Korekcija signala
ecg_corrected = -1 * (ecg_signal - np.mean(ecg_signal))

# 4. Detekcija R-vrhova
peaks, _ = find_peaks(
    ecg_corrected,
    height=np.mean(ecg_corrected) + 2000,
    distance=500
)

# 5. Crtanje
plt.figure(figsize=(15,5))

plt.plot(
    time,
    ecg_corrected,
    color='red',
    linewidth=1,
    label='EKG signal'
)

plt.plot(
    time[peaks],
    ecg_corrected[peaks],
    'kx',
    markersize=8,
    label='R-vrhovi'
)

plt.xlabel("Vrijeme [s]")
plt.ylabel("Amplituda [ADC]")
plt.title("Korigovani EKG signal sa detektovanim R-vrhovima")

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Računanje pulsa
# Računamo razlike u uzorcima
diffs = np.diff(peaks)

# Pretvaramo te razlike u sekunde (fs=1000)
rr_intervals_s = diffs / fs

# Računamo trenutni puls 
# 60 sekundi podijeljeno sa trajanjem JEDNOG intervala daje BPM
instant_bpm = 60 / rr_intervals_s

# Ispisivanje svih vrijednosti
print("Lista svih trenutnih otkucaja u minuti:")
for i, bpm_val in enumerate(instant_bpm):
    print(f"Otkucaj {i+1}: {round(bpm_val, 2)} BPM")

# Dodatna statistika
print(f"Minimalni puls: {round(np.min(instant_bpm), 2)} BPM")
print(f"Maksimalni puls: {round(np.max(instant_bpm), 2)} BPM")
print(f"Prosječan puls: {round(np.mean(instant_bpm), 2)} BPM")

plt.figure(figsize=(12,4))

plt.plot(
    time[peaks][1:],
    instant_bpm,
    '-o'
)

plt.xlabel("Vrijeme [s]")
plt.ylabel("Broj otkucaja [BPM]")
plt.title("Promjena srčanog ritma tokom mjerenja")

plt.grid(True)

plt.tight_layout()

plt.show()

