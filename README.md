# Drone_Detection

This project is for detecting Drone in the presence of Bluetooth interference, in the presence of Wi-Fi signals, in the presence of both and with no interference

It could detect 7 types of Drones and its 3 modes.

Name of Drones are :  new DJI Mavic 2 Air S, DJI Mavic Pro, DJI Mavic Pro 2, DJI Inspire 2, DJI Mavic Mini, DJI Phantom 4, Parrot Disco

And its modes are  :  Switched on, Hovering, Flying
                      
###############################################################   Project Pipiline    ############################################################################

# Data Preprocessing
 - Input of this project is .dat extension file.
 - Done FFT(Fast Fourier Transformation) and SHIFTFFT
 - Result of this step is real or complex vector(belong to whether it is CNN or DC-CNN) that vector length is 2048.
# Data loading and labeling
 - Labeling for its classification problems
    mode : 3 classes (Flying, Hovering, On)
    types : 7 classes (new DJI Mavic 2 Air S, DJI Mavic Pro, DJI Mavic Pro 2, DJI Inspire 2, DJI Mavic Mini, DJI Phantom 4, Parrot Disco)
 - Added load function for training process
# Training Model
 - Suggested and trained 2 models for each DNN(CNN, DC-CNN)
# Predict
 - Input of this system is .dat extension file and output is Drone mode and types
 - Built pipeline for entire system
