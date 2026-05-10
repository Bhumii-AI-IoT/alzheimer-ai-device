# Device Design Rationale

## Artificial Intelligence Enabled Device to Predict Alzheimer's Disease

---

## 1. Design Philosophy

The device was designed around one core idea: monitoring should not 
feel like monitoring.

Alzheimer's patients and people at risk should not have to sit in a 
clinic or wear uncomfortable medical equipment to get useful information 
about their brain health. The goal was to create something that could 
be worn naturally, at home, without disrupting daily life.

That thinking shaped every design decision — the form factor, the 
sensor placement, the frame structure, and the overall look of the device.

---

## 2. Why a Visor

A head-mounted visor was chosen for practical reasons, not aesthetic ones.

The head is the only place on the body where both EEG signals and eye 
movements can be captured simultaneously without separate devices. 
Placing everything in one wearable means:

- The person only needs to put on one thing
- Sensor positioning stays consistent across sessions
- Data from both modalities is captured at the same time

A wraparound structure was chosen over a headband or cap because it 
provides stable contact at the temples and forehead without adhesive 
electrodes or gel — making it realistic for home use.

---

## 3. Sensor Placement

| Sensor | Placement | Reason |
|--------|-----------|--------|
| EEG dry electrodes | Inner frame, temples and forehead | Frontal and temporal lobe activity |
| IR eye-tracking sensor | Front lens panel | Direct line of sight to both eyes |
| Processing unit | Rear frame | Weight balance across the head |

---

## 4. Why Dry Electrodes

Traditional EEG uses wet gel electrodes applied to the scalp. They 
produce high quality signals but are messy, time consuming to set up, 
and completely impractical for daily home use.

Dry electrodes are less precise but far more usable. For a device 
designed to monitor patterns over time — not capture a single clinical 
snapshot — consistency of use matters more than perfect signal quality 
in any one session.

---

## 5. Original Design

The visual appearance and physical form factor of this device is an 
original concept developed and designed by the author. The software 
and documentation in this repository are licensed under the MIT Licence.

---

## 6. What This Design Does Not Solve Yet

Being honest about limitations is part of good design documentation.

| Current Limitation | What is Needed Next |
|-------------------|---------------------|
| No physical hardware prototype yet | Component sourcing and assembly |
| Dry electrode signal quality is lower than clinical EEG | Signal processing to compensate |
| One size frame | Adjustable sizing for different head sizes |
| No wireless streaming yet | Bluetooth LE integration |

These are not failures — they are the next steps. The design concept 
is sound. The engineering work to realise it is the next phase.

---

## 7. Clinical and Ethical Considerations

This device collects neurological and biometric data. That comes with 
responsibility.

- User consent must be explicit and informed before any data is collected
- Data should be processed locally where possible — not stored in the 
  cloud unnecessarily
- The device is a support tool for early detection — it is not a 
  replacement for clinical diagnosis
- Any future human participant study will require full ethics review

These principles are built into the design from the beginning, not 
added later.