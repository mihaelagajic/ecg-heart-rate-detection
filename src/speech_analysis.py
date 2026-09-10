import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import pandas as pd


# 1. Učitavanje audio signala

audio_path = r'Audio and ECG-20260611T153310Z-3-001\Audio and ECG\Zmaj 1 relaxed\Zmaj 1 relaxed.wav'

signal, sr = librosa.load(
    audio_path,
    sr=None
)

print("Frekvencija odabiranja:", sr)
print("Trajanje signala:", len(signal)/sr, "s")


# 2. Prikaz vremenskog oblika signala

time = np.arange(len(signal))/sr

plt.figure(figsize=(12,4))
plt.plot(time, signal)

plt.xlabel("Vrijeme [s]")
plt.ylabel("Amplituda")
plt.title("Vremenski oblik audio signala govora")
plt.grid(True)
plt.tight_layout()
plt.show()



# ---------------------------------------
# 3. MFCC karakteristike
# ---------------------------------------

mfcc = librosa.feature.mfcc(
    y=signal,
    sr=sr,
    n_mfcc=13
)


D = librosa.amplitude_to_db(
    np.abs(librosa.stft(signal)),
    ref=np.max
)

plt.figure(figsize=(12,5))

librosa.display.specshow(
    D,
    sr=sr,
    x_axis='time',
    y_axis='hz',
    cmap='viridis'
)

cbar=plt.colorbar()
cbar.set_label("Amplituda [dB]")

plt.title("Spektrogram audio signala")

plt.tight_layout()

plt.show()

plt.figure(figsize=(12,4))

librosa.display.specshow(
    mfcc,
    x_axis='time',
    sr=sr,
    cmap='jet'
)

cbar=plt.colorbar()

cbar.set_label("MFCC")

plt.ylabel("MFCC koeficijent")

plt.title("MFCC karakteristike audio signala")

plt.tight_layout()

plt.show()

mfcc_mean = np.mean(mfcc, axis=1)
mfcc_std = np.std(mfcc, axis=1)


print("Srednje vrijednosti MFCC:")
print(mfcc_mean)

print("Standardne devijacije MFCC:")
print(mfcc_std)



# ---------------------------------------
# 4. RMS energija
# ---------------------------------------

rms = librosa.feature.rms(
    y=signal
)


plt.figure(figsize=(10,4))

plt.plot(
    librosa.times_like(rms, sr=sr),
    rms[0]
)

plt.xlabel("Vrijeme [s]")
plt.ylabel("RMS energija")
plt.title("Promjena energije govornog signala")

plt.grid(True)

plt.show()



print("Srednja RMS energija:",
      np.mean(rms))



# ---------------------------------------
# 5. Zero Crossing Rate
# ---------------------------------------

zcr = librosa.feature.zero_crossing_rate(
    signal
)


plt.figure(figsize=(10,4))

plt.plot(
    librosa.times_like(zcr, sr=sr),
    zcr[0]
)

plt.xlabel("Vrijeme [s]")
plt.ylabel("ZCR")
plt.title("Zero Crossing Rate audio signala")

plt.grid(True)

plt.show()



print("Srednji ZCR:",
      np.mean(zcr))



# ==========================
# Procjena osnovne frekvencije (Pitch)
# ==========================

# Procena F0 pomoću YIN algoritma
pitch = librosa.yin(
    y=signal,
    fmin=50,      # Minimalna očekivana frekvencija glasa
    fmax=400,     # Maksimalna očekivana frekvencija glasa
    sr=sr
)

# Uklanjanje nevažećih vrijednosti
pitch = pitch[np.isfinite(pitch)]

# Srednja vrijednost Pitch-a
print(f"Srednja osnovna frekvencija glasa: {np.mean(pitch):.2f} Hz")

# Vremenska osa
times = librosa.times_like(pitch, sr=sr)

# Grafički prikaz
plt.figure(figsize=(12,4))

plt.plot(times, pitch, color='blue')

plt.xlabel("Vrijeme [s]")
plt.ylabel("Frekvencija [Hz]")
plt.title("Promjena osnovne frekvencije glasa (Pitch)")

plt.grid(True)
plt.tight_layout()
plt.show()


# ---------------------------------------
# 7. Spektralni centroid
# ---------------------------------------

centroid = librosa.feature.spectral_centroid(
    y=signal,
    sr=sr
)


plt.figure(figsize=(10,4))

plt.plot(
    librosa.times_like(centroid, sr=sr),
    centroid[0]
)

plt.xlabel("Vrijeme [s]")
plt.ylabel("Frekvencija [Hz]")
plt.title("Spektralni centroid audio signala")

plt.grid(True)

plt.show()

print("Srednji spektralni centroid:",
      np.mean(centroid),
      "Hz")

results = pd.DataFrame({

    'Karakteristika': [

        'RMS',
        'Zero Crossing Rate',
        'Pitch',
        'Spectral Centroid'

    ],

    'Srednja vrijednost': [

        np.mean(rms),
        np.mean(zcr),
        np.mean(pitch),
        np.mean(centroid)

    ],

    'Standardna devijacija': [

        np.std(rms),
        np.std(zcr),
        np.std(pitch),
        np.std(centroid)

    ]

})

print(results)
