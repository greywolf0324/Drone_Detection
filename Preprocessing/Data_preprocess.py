### Produced by Carolyn J. Swinney and John C. Woods for use with the 'DroneDetect' dataset ###

import os
import numpy as np
from numpy import sum,isrealobj,sqrt
from numpy.random import standard_normal
from numpy.fft import fft, fftshift
import json

file = "E:\work\Daily/c_14\preprocessing"                            # path to file location

INTERF = ['BOTH', 'BLUE', 'WIFI', 'CLEAN']
# DRONE_EXCEPT = ['DIS']
DRONE_NAME = ['AIR', 'INS', 'MIN', 'MP1', 'MP2', 'PHA', 'DIS']
MODE = ['FY', 'HO', 'ON']

# BUI = []
# # BUI{1,1} = {'000000'};                                # BUI of RF background activities
# BUI.append(['100000', '100001', '100010'])              # DJI Mavic 2 Air S
# BUI.append(['100100', '100110'])                        # the Parrot Disco 
# BUI.append(['101000', '101001', '101010'])              # DJI Inspire 2
# BUI.append(['101100', '101101', '101110'])              # DJI Mavic Mini
# BUI.append(['110000', '110001', '110010'])              # DJI Mavic Pro
# BUI.append(['110100', '110101', '110110'])              # DJI Mavic Pro 2
# BUI.append(['111000', '111001', '111010'])              # DJI Phantom 4

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

EXC_MODE = {
    'ON' : '00',
    'HO' : '01',
    'FY' : '10'
}
M = 2048; # Total number of frequency bins
L = 1e6;  # Total number samples in a segment
Q = 10;   # Number of returning points for spectral continuity
           
for interf in INTERF :
    print("========================================")
    for name in DRONE_NAME :
        print("_______________________________________")
        for mode in MODE :
            print("#################################")
            Data = []
            print(name, mode)
            if not (name == 'DIS' and mode == 'HO') :
            
                for i in range(5) :
                    print("file ", i + 1, "...")
                    file_path = file + '\\' + interf + '\\' + name + '_' + mode + '\\' + name + '_' + BUI_NAME[interf] + BUI_MODE[mode] + '_0' + str(i) + '.dat' 
                    print(file_path)
                    H_ = []
                    L_ = []

                    f = open(file_path, "rb")                                        # open file
                    data = np.fromfile(f, dtype="float32",count=240000000)      # read the data into numpy array


                    data = data.reshape(int(len(data) / 2), 2)
                    data = np.hsplit(data, 2)
                    L_ = data[0]
                    H_ = data[1]
                    print(L_)
                    
                    for j in range(int(len(L_) / L)) :
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
                
                DATA = np.power(Data, 2)

                with open(f"{interf}_{name}_{mode}.txt", "w") as fp:
                    json.dump(DATA.tolist(), fp)  # encode dict into JSON
                

            
            