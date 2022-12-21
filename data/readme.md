# Data description

Data from children with autism is in the ASD folder; data from typically developing peers is in the TD folder. The files with each participant’s resting state data are .csv files (extension .asc does not matter). Recording frequency (256Hz or 512 Hz) is noted in the file name. The durations of the recordings differ (between 1.5 to 3 minutes). There are 32 electrodes + 2 eye channels in each file, listed in columns (34 columns total); the first row is the name of the electrode, for example, C3-LkE (the –LkE part isn’t meaningful).

- Data for participants TD102 and TD 103 were recorded using a cap with 24 electrodes only.

Electrodes of the left hemisphere have odd numbers (1, 3, 5…), those of the right hemisphere are even. The setup is, roughly, like in the picture; the additional channels are POz (between Pz and Oz on the central line), M1 and M2 (ground and reference electrode, behind the ears), and HEOG and VEOG – those are eye channel electrodes.
Meaningful comparisons for interhemispheric oscillatory synchrony would be between pairs of electrodes with the same name, and matching numbers: FP1/2, F3/4, F7/8, FC1/2, FC5/6, C3/4, CP1/2, CP5/6, P3/4, P7/8, O1/2. Temporal channels (T7/T8 in the file) are often noisy (close to the muscle that is engaged in jaw-clenching).
With regard to frequency activity, the breakdown for bands is as follows:

- **Delta wave** – (0.1 – 4 Hz)

- **Theta wave** – (4 – 7 Hz)

- **Alpha wave** – (8 – 12 Hz) – there is a body of literature that insists on identifying alpha range specifically for each patient (i.e. the peak power can be lower or higher), but only for this type.

- **Beta waves** - (15 – 30 Hz), although can be broken down into:

  - **Low Beta** Waves (12.5–16 Hz, "Beta 1 power");
  - **Beta Waves** (16.5–20 Hz, "Beta 2 power")
  - **High Beta** Waves (20.5–28 Hz, "Beta 3 power").

- **Gamma wave** – (32 – 100 Hz) – can be broken down into low (30-60) and high (60-100, although the recording allows analysis up to 128 Hz (256 Hz recording), or 256Hz (512 Hz recording) – the concern at high frequencies is muscle artifact, which is expected to have higher power than brain-produced gamma).
