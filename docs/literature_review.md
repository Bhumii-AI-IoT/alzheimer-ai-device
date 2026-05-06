# Literature Review

## EEG and Eye-Tracking Biomarkers for Alzheimer's Disease Detection

---

## 1. Background

Alzheimer's Disease is a progressive neurodegenerative disorder and the 
most common cause of dementia globally. Its pathological changes begin 
accumulating in the brain 10 to 20 years before clinical symptoms emerge. 
This makes early, pre-symptomatic detection one of the most important 
frontiers in neurological research.

The challenge is that current diagnostic tools — MRI scans, cognitive 
assessments, spinal fluid tests — are expensive, invasive, and typically 
only used after symptoms have already appeared. By that point, significant 
neurological damage has already occurred.

This review explores two non-invasive signal types — EEG brainwave 
patterns and eye movement behaviour — as potential early biomarkers that 
could be captured continuously through a wearable device.

---

## 2. EEG Biomarkers

### What changes in an Alzheimer's brain

Research consistently shows measurable differences in brainwave activity 
between healthy ageing brains and those affected by Alzheimer's:

- **Increased slow wave activity** — delta (0.5–4 Hz) and theta (4–8 Hz) 
  bands show elevated power in Alzheimer's patients
- **Decreased fast wave activity** — alpha (8–13 Hz) and beta (13–30 Hz) 
  bands are reduced
- **Slowing of dominant frequency** — the brain's peak operating frequency 
  shifts downward
- **Reduced connectivity** — synchronisation between different brain 
  regions weakens

These changes are detectable through electroencephalography (EEG) — 
a non-invasive method of recording electrical activity on the scalp.

### Why this matters for the device

The visor's dry EEG electrodes, positioned at the temples and forehead, 
are designed to capture frontal and temporal lobe activity — the regions 
most associated with memory and early Alzheimer's changes.

---

## 3. Eye-Tracking Biomarkers

### Saccadic eye movements

Saccades are the rapid, jumping movements your eyes make when shifting 
focus from one point to another. In Alzheimer's patients:

- Saccades are slower and less accurate
- The time taken to initiate a saccade increases
- Errors increase when patients are asked to look away from a stimulus

### Smooth pursuit

When following a slowly moving object, Alzheimer's patients show reduced 
accuracy — the eye fails to keep pace with the target smoothly.

### Blink rate and pupil response

Spontaneous blink rate and pupillary light reflex have both shown 
abnormalities in neurodegenerative conditions. Reduced blink rates and 
slower pupil constriction have been observed in early-stage patients.

### Why this matters for the device

The visor's front lens houses an infrared eye-tracking sensor with a 
direct line of sight to both eyes — capturing these movement patterns 
passively during normal wear.

---

## 4. AI and Machine Learning Approaches

Multiple studies have applied machine learning to EEG and eye-tracking 
data for Alzheimer's classification:

- **Random Forests and SVMs** have been used for EEG feature 
  classification with accuracy ranges of 75–90% in controlled studies
- **Convolutional Neural Networks** applied to raw EEG spectrograms 
  have shown promise
- **Multimodal fusion** — combining EEG and eye-tracking — consistently 
  outperforms single-modality approaches

This is the core technical rationale for combining both sensors in 
this device.

---

## 5. Research Gap This Project Addresses

Most studies in this area are conducted in clinical laboratories using 
expensive, uncomfortable wet-electrode EEG caps. Results are obtained 
in controlled, artificial environments — not in the real world where 
people actually live.

This project explores whether the same biomarker signals can be captured 
through a comfortable, home-use wearable — making early detection 
accessible outside of a hospital setting.

---

## 6. Key References

*(To be updated)*

1. Jeong, J. (2004). EEG dynamics in patients with Alzheimer's disease. 
   *Clinical Neurophysiology*, 115(7), 1490–1505.
2. Babiloni, C. et al. (2020). Measures of resting state EEG and 
   Alzheimer's disease. *Clinical Neurophysiology*.
3. Moeller, S. et al. (2011). Eye movement abnormalities in 
   neurodegenerative disease. *Current Neurology and Neuroscience Reports*.
4. Martínez-Murcia, F.J. et al. (2019). Deep learning applied to EEG 
   for Alzheimer's detection. *Complexity*.