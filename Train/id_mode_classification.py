from keras.layers.core import Reshape
from sklearn.model_selection import StratifiedKFold
from keras.layers import Dense, Dropout
from sklearn.metrics import f1_score, accuracy_score, precision_score, recall_score, confusion_matrix
import numpy as np
from keras.utils import to_categorical
from keras.models import Sequential
from keras import regularizers
from keras.layers import Dense
from keras.layers import Conv1D,MaxPooling1D, Flatten,AveragePooling1D
from keras import optimizers
import json
from Loading.data_labeling import labeling
from load_data import load_id_mode


def decode(datum) :
    y = np.zeros((datum.shape[0],1))
    for i in range(datum.shape[0]):
        y[i] = np.argmax(datum[i])
    return y
def encode(datum) :
    return to_categorical(datum)

adam = optimizers.Adam(lr=0.00001, beta_1=0.9, beta_2=0.999,amsgrad=False)

np.random.seed(1)
K                    = 10
inner_activation_fun = 'relu'
outer_activation_fun = 'sigmoid'
optimizer_loss_fun   = 'mse'
optimizer_algorithm  = 'adam'
number_inner_layers  = 3
number_inner_neurons = 256
number_epoch         = 20
batch_length         = 10
show_inter_results   = 2

INTERF = ['BOTH', 'BLUE', 'WIFI', 'CLEAN']
# DRONE_EXCEPT = ['DIS']
DRONE_NAME = ['AIR', 'INS', 'MIN', 'MP1', 'MP2', 'PHA', 'DIS']
MODE = ['FY', 'HO', 'ON']

# load preprocessed data for training
print("loading x...")
x = load_id_mode(["BOTH"], DRONE_NAME, MODE)

print("loading y...")
y = labeling()[3]


X = np.array([item for sublist in x for item in sublist])
Y = np.array([item for sublist in y for item in sublist])
Y = encode(Y)

train_X = X.reshape(-1, 2048, 1)


print(train_X.shape, Y.shape)

cvscores    = []
cnt         = 0
kfold = StratifiedKFold(n_splits=K, shuffle=True, random_state=1)

print("Starting?")
#########################################################################
for train, test in kfold.split(train_X, decode(Y)) :
    cnt = cnt + 1
    print(cnt)
    cnn = Sequential()
    print(X.shape[0],1)
    print('x_train shape:', X[train].shape)
    print(Y.shape[0],1)
    print("y_train shape:", Y[train].shape)
    
    cnn = Sequential()
    cnn.add(Conv1D(32,kernel_size=3,activation='relu',input_shape=(2048,1),padding='same'))
    
    cnn.add(Conv1D(32,kernel_size=3,  activation='relu',padding='same'))
    cnn.add(AveragePooling1D(pool_size=3))
    
    cnn.add(Conv1D(64,3, activation='relu',padding='same'))
    cnn.add(AveragePooling1D(3))
    
    cnn.add(Conv1D(64,3,  activation='relu',padding='same'))
    cnn.add(Conv1D(128,3, activation='relu',padding='same'))
    cnn.add(Conv1D(128,3, activation='relu',padding='same'))
    cnn.add(AveragePooling1D(3))

    cnn.add(Conv1D(64,3, activation='relu',padding='same'))
    cnn.add(Dropout(0.2))

    cnn.add(Flatten())
    cnn.add(Dense(256, activation = inner_activation_fun))
    cnn.add(Dense(20,activation='softmax'))

    print(cnn.summary())
    print('Compiling')
    cnn.compile(loss = 'categorical_crossentropy', optimizer = optimizer_algorithm, metrics =         ['accuracy'])
    print('Compilation is complete')
    print('fitting the model')
    
    #cnn.fit(x[train], y[train], epochs = number_epoch, batch_size = batch_length, verbose = show_inter_results)
    cnn.fit(X[train], Y[train], batch_size=batch_length , epochs=number_epoch ,verbose=show_inter_results)
    #cnn.fit(x[train], y[train],batch_size=batch_length,epochs=number_epoch,verbose = show_inter_results)
    #print(cnn.summary())

    print('fitting complete \n Evaluating:')
    scores = cnn.evaluate(X[test], Y[test], verbose = show_inter_results)
    print(scores[1]*100)
    cvscores.append(scores[1]*100)
    print('Predicting the final results')
    y_pred = cnn.predict(X[test]).argmax(axis=1)
    rounded_predictions = cnn.predict(X[test],verbose=1).argmax(axis=1)
    rounded_labels=np.argmax(Y[test], axis=1)
    print('Precision: ',precision_score(rounded_labels, rounded_predictions, average="macro"))
    print('Recall: ',recall_score(rounded_labels, rounded_predictions, average="macro"))
    print('F1_Score: ',f1_score(rounded_labels, rounded_predictions, average="macro"))
    print('Accuracy: ',accuracy_score(rounded_labels, rounded_predictions))
    cm = confusion_matrix(rounded_labels, rounded_predictions)
    print(cm)
    cnn.save(f"model_{cnt}.keras")
    # np.savetxt("Classification_Results_450epoch\\Results_3%s.csv" % cnt, np.column_stack((Y[test], y_pred)), delimiter=",", fmt='%s')
#########################################################################
