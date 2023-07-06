from Preprocessing.load_preprocess import preprocess_data
import numpy as np
from keras.models import load_model
from list_maxcount import max_occur

clas_type = {
    0 : "AIR",
    1 : "INS",
    2 : "MIN",
    3 : "MP1",
    4 : "MP2",
    5 : "PHA",
    6 : "DIS"
}

clas_mode = {
    0 : "FY",
    1 : "ON",
    2 : "HO"
}

def predict(typemodel_path, modemodel_path, data_path) :
    
    typemodel = load_model(typemodel_path)
    modemodel = load_model(modemodel_path)
    
    processed_input = preprocess_data(data_path)


    input = np.array([np.array(processed_input[0])])
    
    # print(len(processed_input))
    inputs = []
    types = []
    modes = []
    
    for i in range(20) :
        inputs.append(np.array([np.array(processed_input[i])]))

    for temp in inputs :
        pred_type = typemodel(temp)
        pred_mode = modemodel(temp)
        
        res_type = np.where(pred_type[0] == np.amax(pred_type[0]))[0][0]
        res_mode = np.where(pred_mode[0] == np.amax(pred_mode[0]))[0][0]
        
        print(res_type, clas_type[res_type])
        print(res_mode, clas_mode[res_mode])
        
        types.append(clas_type[res_type])
        modes.append(clas_mode[res_mode])
        
    print("output ensemble result : ", f"type - {max_occur(types)} ", f"mode - {max_occur(modes)}")
    print("##################")
     
    pred_type = typemodel(input)
    pred_mode = modemodel(input)
    
    res_type = np.where(pred_type[0] == np.amax(pred_type[0]))[0][0]
    res_mode = np.where(pred_mode[0] == np.amax(pred_mode[0]))[0][0]

    print(res_type, clas_type[res_type])
    print(res_mode, clas_mode[res_mode])
    
   

