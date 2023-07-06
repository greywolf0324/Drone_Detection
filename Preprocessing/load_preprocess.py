from numpy.fft import fft, fftshift
# import json
import numpy as np

BUI_NAME = {
    'BOTH' : '11',
    'BLUE' : '01',
    'WIFI' : '10',
    'CLEAN' : '00'
}

BUI_MODE = {
    'ON' : '00',
    'HO' : '01',
    'FY' : '10'
}


def preprocess_data(file_path) :
    M = 2048; # Total number of frequency bins
    L = 1e6;  # Total number samples in a segment
    Q = 10;   # Number of returning points for spectral continuity

    H_ = []
    L_ = []
    f = open(file_path, "rb")                                        # open file
    data = np.fromfile(f, dtype="float32",count=240000000)      # read the data into numpy array


    data = data.reshape(int(len(data) / 2), 2)
    data = np.hsplit(data, 2)
    L_ = data[0]
    H_ = data[1]

    Data = []
    for j in range(20) :
        print(" step", j + 1, "...")
        st = int(j * L)
        fi = int((j + 1) * L)
        
        print("     x...")
        
        xf = L_[st : fi] - np.mean(L_[st : fi])
        xf = np.abs(fftshift(fft([item for sublist in xf for item in sublist], M)))
        xf = xf[int(len(xf) / 2) :]
        
        print("     y...")
        
        yf = H_[st : fi] - np.mean(H_[st : fi])
        yf = np.abs(fftshift(fft([item for sublist in yf for item in sublist], M)))
        yf = yf[int(len(yf) / 2) :]
        
        mean_xf = np.mean(xf[(len(xf)-Q):])
        mean_yf = np.mean(yf[:Q])
        
        Data.append(np.concatenate((xf, (yf * mean_xf / mean_yf))))

    return np.power(Data, 2)
