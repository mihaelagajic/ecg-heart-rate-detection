import matplotlib.pyplot as plt

labels = [
    "Z1 R",
    "Z1 S",
    "Z2 R",
    "Z2 S"
]

rms = [
    0.036219,
    0.030315,
    0.036333,
    0.031425
]

plt.figure(figsize=(7,4))
plt.bar(labels, rms)

plt.ylabel("RMS energija")
plt.xlabel("Audio snimak")
plt.title("Poređenje srednje RMS energije")

plt.grid(axis='y')
plt.tight_layout()
plt.show()

pitch = [
169.294,
165.732,
174.879,
165.383
]

plt.figure(figsize=(8,5))

plt.bar(labels, pitch)

plt.title("Poređenje srednje osnovne frekvencije glasa")

plt.xlabel("Audio snimak")

plt.ylabel("Pitch [Hz]")

plt.grid(axis='y')

plt.tight_layout()

plt.show()

centroid = [
2595.663,
2428.919,
2416.651,
2542.225
]

plt.figure(figsize=(8,5))

plt.bar(labels, centroid)

plt.title("Poređenje srednjeg spektralnog centroida")

plt.xlabel("Audio snimak")

plt.ylabel("Spektralni centroid [Hz]")

plt.grid(axis='y')

plt.tight_layout()

plt.show()

labels = [
    "Zmaj 1\nRelaxed",
    "Zmaj 1\nStres",
    "Zmaj 2\nRelaxed",
    "Zmaj 2\nStres"
]

zcr = [
    0.061629,
    0.052382,
    0.054147,
    0.055521
]

plt.figure(figsize=(8,5))

plt.bar(labels, zcr)

plt.title("Poređenje srednje vrijednosti Zero Crossing Rate")

plt.xlabel("Audio snimak")

plt.ylabel("Zero Crossing Rate")

plt.grid(axis='y')

plt.tight_layout()

plt.show()

labels = [
    "Zmaj 1\nRelaxed",
    "Zmaj 1\nStres",
    "Zmaj 2\nRelaxed",
    "Zmaj 2\nStres"
]

mfcc1 = [-398.17288, -405.11487, -393.73530, -406.05410]
mfcc2 = [134.57880, 135.99075, 138.22717, 146.50291]
mfcc3 = [-2.6172953, 6.1123509, -0.8914579, -6.0822477]

fig, ax = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# MFCC1
ax[0].bar(labels, mfcc1)
ax[0].set_title("MFCC1")
ax[0].set_ylabel("Vrijednost")
ax[0].grid(axis='y')

# MFCC2
ax[1].bar(labels, mfcc2)
ax[1].set_title("MFCC2")
ax[1].set_ylabel("Vrijednost")
ax[1].grid(axis='y')

# MFCC3
ax[2].bar(labels, mfcc3)
ax[2].set_title("MFCC3")
ax[2].set_ylabel("Vrijednost")
ax[2].set_xlabel("Audio snimak")
ax[2].grid(axis='y')

fig.suptitle("Poređenje srednjih vrijednosti MFCC koeficijenata", fontsize=14)

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
