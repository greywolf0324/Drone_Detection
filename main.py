from predict import predict, predict_complex

CNN_typemodel_path = "Models/1D_CNN/type/model_40_90_66_con3_drop_k5_den64.keras"
CNN_modemodel_path = "Models/1D_CNN/mode/model_50_96_67_con3_drop_k3.keras"

DCCNN_typemodel_path = ""
DCCNN_modemodel_path = "Models\DC_CNN\mode/DC_mode_151_156.keras"

data_path = "E:\work\Daily\.RECENT/6_14\preprocessing\BOTH\DIS_ON/DIS_1100_02.dat"

predict(CNN_typemodel_path, CNN_modemodel_path, data_path)

# predict_complex(DCCNN_modemodel_path, data_path)