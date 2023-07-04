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
from load_data import load_mode
from Loading.data_labeling import labeling_mode
from Loading.spliting import spliting
import complexnn
from keras import models
from keras import layers
from keras import optimizers

class_count = 7

def decode(datum) :
    y = np.zeros((datum.shape[0],1))
    for i in range(datum.shape[0]):
        y[i] = np.argmax(datum[i])
    return y
def encode(datum) :
    return to_categorical(datum)

INTERF = ['BOTH', 'BLUE', 'WIFI', 'CLEAN']
# DRONE_EXCEPT = ['DIS']
DRONE_NAME = ['AIR', 'INS', 'MIN', 'MP1', 'MP2', 'PHA', 'DIS']
MODE = ['FY', 'HO', 'ON']

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
number_class         = 3
x = load_mode(["BOTH"], DRONE_NAME, MODE)

for i, temp in enumerate(x) :
    for j, temp_1 in enumerate(temp) :
        tem = x[i][j]
        x[i].pop(j)
        x[i].insert(j, spliting(tem))
        

y = labeling_mode()

X = np.array([item for sublist in x for item in sublist])
Y = np.array([item for sublist in y for item in sublist])
Y = encode(Y)

train_X = X.reshape(-1, 2048, 1)

print(type(x), type(x[0]), type(x[0][0]))
print(len(x), len(x[0]), len(x[0][0]))

print(type(X), type(X[0]), type(X[0][0]))
print(len(X), len(X[0]), )

print(train_X.shape, Y.shape)

cvscores    = []
cnt         = 0
kfold = StratifiedKFold(n_splits=K, shuffle=True, random_state=1)

print("Starting?")

for train, test in kfold.split(train_X, decode(Y)) :
    cnt = cnt + 1
    print(cnt)
    model = models.Sequential()

    model.add(complexnn.conv.ComplexConv1D(128, kernel_size=16, activation = 'relu', input_shape = (1024, 2), padding='same'))
    model.add(layers.Dropout(0.35))
    model.add(complexnn.conv.ComplexConv1D(64, kernel_size=8, activation = 'relu', padding='same'))
    model.add(layers.Dropout(0.35))
    # model.add(layers.Flatten())
    model.add(layers.Dense(256, activation='softmax'))
    model.add(layers.Dense(128, activation='softmax'))
    model.add(layers.Dense(class_count, activation = 'softmax'))
    # model.add(complexnn.bn.ComplexBatchNormalization())
    # model.add(layers.MaxPool2D((2, 2), padding = 'same'))

    model.compile(optimizer = optimizers.Adam(), loss = 'mse')
    print('Compiling')
    print(model.summary())
        
    print('Compilation is complete')
    print('fitting the model')
    
    #cnn.fit(x[train], y[train], epochs = number_epoch, batch_size = batch_length, verbose = show_inter_results)
    model.fit(X[train], Y[train], batch_size=batch_length , epochs=number_epoch ,verbose=show_inter_results)
    #cnn.fit(x[train], y[train],batch_size=batch_length,epochs=number_epoch,verbose = show_inter_results)
    #print(cnn.summary())

    print('fitting complete \n Evaluating:')
    scores = model.evaluate(X[test], Y[test], verbose = show_inter_results)
    print(scores[1]*100)
    cvscores.append(scores[1]*100)
    print('Predicting the final results')
    y_pred = model.predict(X[test]).argmax(axis=1)
    rounded_predictions = model.predict(X[test],verbose=1).argmax(axis=1)
    rounded_labels=np.argmax(Y[test], axis=1)
    print('Precision: ',precision_score(rounded_labels, rounded_predictions, average="macro"))
    print('Recall: ',recall_score(rounded_labels, rounded_predictions, average="macro"))
    print('F1_Score: ',f1_score(rounded_labels, rounded_predictions, average="macro"))
    print('Accuracy: ',accuracy_score(rounded_labels, rounded_predictions))
    cm = confusion_matrix(rounded_labels, rounded_predictions)
    print(cm)
    model.save(f"model_{cnt}.keras")