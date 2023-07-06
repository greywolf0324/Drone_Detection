from predict import predict

CNN_typemodel_path = "Models/1D_CNN/type/model_40_90_66_con3_drop_k5_den64.keras"
CNN_modemodel_path = "Models/1D_CNN/mode/model_50_96_67_con3_drop_k3.keras"

DCCNN_typemodel_path = ""
DCCNN_modemodel_path = ""

data_path = ""

predict(CNN_typemodel_path, CNN_modemodel_path, data_path)