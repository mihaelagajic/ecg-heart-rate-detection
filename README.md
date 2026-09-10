# ECG-Based Heart Rate Analysis and Speech Signal Processing

## Overview

This project investigates whether speech signals contain acoustic characteristics that can be related to changes in heart rate.

During the experiment, ECG and speech signals were recorded simultaneously while subjects read predefined texts in different physiological and emotional conditions. The ECG signal was used as a reference for heart-rate estimation, while the corresponding speech recordings were analyzed to extract acoustic features.

The main goal was to investigate whether heart rate could be reliably estimated from speech-related characteristics.

## Research Questions

* Can acoustic characteristics of speech be related to heart rate?
* Which speech features show the greatest changes between relaxed and stressed conditions?
* Is there a consistent relationship between speech characteristics and heart rate?
* Can speech provide a reliable basis for non-contact heart-rate estimation?

## Methodology

The analysis consists of two main parts.

### 1. ECG Signal Processing

The ECG signal was processed using Python and SciPy.

The following steps were performed:

* loading the recorded ECG signal,
* removal of the signal mean and baseline offset,
* correction of signal polarity,
* detection of R-peaks,
* calculation of RR intervals,
* conversion of RR intervals to beats per minute (BPM),
* calculation of minimum, maximum and average heart rate,
* visualization of heart-rate changes over time.

The ECG-derived heart rate was used as the reference value for comparison with speech characteristics.

### 2. Speech Signal Processing

The speech recordings were analyzed using Python and Librosa.

The following acoustic features were extracted:

* Mel-Frequency Cepstral Coefficients (MFCC),
* RMS energy,
* Zero Crossing Rate (ZCR),
* fundamental frequency (Pitch),
* spectral centroid,
* spectrogram.

Mean values and standard deviations of the extracted features were calculated for further comparison.

## Technologies

* Python
* NumPy
* Pandas
* SciPy
* Librosa
* Matplotlib
* Jupyter Notebook

## Results

The analysis showed that some speech characteristics changed between relaxed and stressed conditions.

MFCC features showed the most consistent changes between the analyzed conditions. RMS energy and Pitch also showed similar trends for the analyzed subjects, while ZCR and spectral centroid did not exhibit a consistent trend.

However, no clear one-to-one relationship between individual speech characteristics and heart rate was established.

The results therefore suggest that speech contains information related to physiological state, but the analyzed dataset is not sufficient to reliably estimate heart rate from individual acoustic features alone.

A larger dataset, more subjects, additional speech features and statistical or machine-learning methods would be required for a more reliable heart-rate estimation model.

## Project Report

A detailed description of the methodology, signal processing procedures, results, discussion and limitations is available in the full project report:

**[Full Project Report](report/report.pdf)**

## Limitations

The study was based on a limited number of recordings and subjects. The speech material was predefined and the physiological response to stress may differ between individuals.

The analysis mainly considered average feature values, while a more detailed time-dependent analysis and statistical modeling could provide additional information.

## Future Work

Possible extensions of the project include:

* analysis of a larger dataset,
* time-synchronized comparison of ECG and speech features,
* correlation analysis,
* extraction of additional speech features,
* feature selection,
* machine-learning models for heart-rate estimation,
* evaluation on unseen subjects.

## Academic Context

This project was developed as part of the **Clinical Engineering** course at the University of Belgrade – School of Electrical Engineering (ETF), during the 2025/2026 academic year.
