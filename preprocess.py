import mne
from pathlib import Path 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def getInput(file):    
    all_epochs = mne.read_epochs(Path('out_data') / file )
    idx_asd = all_epochs.events[:, 2] == all_epochs.event_id['asd']
    idx_td = all_epochs.events[:, 2] == all_epochs.event_id['td']

    # trails (epochs, channels, samples)
    np_all_epochs = all_epochs.get_data()

    print(f"epochs: {np_all_epochs.shape[0]}, channels: {np_all_epochs.shape[1]}, samples: {np_all_epochs.shape[2]}")
    n_trials = np_all_epochs.shape[0]

    # Labels
    y = np.empty(len(all_epochs.events), dtype=int)  

    # Encode: ASD = 0, TD = 1.
    y[idx_asd] = 0
    y[idx_td] = 1

    return all_epochs, idx_asd, idx_td, np_all_epochs, y

# Get input that includes extracted features
def getProcessedInput(featureCount, fmax, np_all_epochs, all_epochs, featureExtractor):
    X_2d = np.empty([np_all_epochs.shape[0], np_all_epochs.shape[1], featureCount], dtype=float)
    psd_epochs_channels_freqs = all_epochs.compute_psd(fmax=fmax).get_data()  
    for epoch_id, epoch in enumerate(psd_epochs_channels_freqs):
        for channel_id, channel in enumerate(epoch):
            X_2d[epoch_id, channel_id, :] = featureExtractor(channel)

    n_trials = np_all_epochs.shape[0]
    #X_2d_reshaped = X_2d.reshape(n_trials, -1)
    # X_2d_reshaped
    return X_2d