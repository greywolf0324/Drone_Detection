import json
import numpy as np

INTERF = ['BOTH', 'BLUE', 'WIFI', 'CLEAN']
# DRONE_EXCEPT = ['DIS']
DRONE_NAME = ['AIR', 'INS', 'MIN', 'MP1', 'MP2', 'PHA', 'DIS']
MODE = ['FY', 'HO', 'ON']
drone_mode = {'FY':0, 'ON':1, 'HO':2}
drone_name = {'AIR':0, 'INS':1, 'MIN':2, 'MP1':3, 'MP2':4, 'PHA':5, 'DIS':6}
def labeling() :
    label = []
    
    detection = []
    identification = []
    mode_state = []
    inter = []
    groups = []
    for interf in ["BOTH"] :
        for name in DRONE_NAME :
            for mode in MODE :
                if not (name == 'DIS' and mode == 'HO') :
                    with open(f"{interf}_{name}_{mode}.txt", "r") as fp:
                        length = len(json.load(fp))
                        print(f"    {interf}_{name}_{mode} ...")
                        groups.append(drone_mode[mode])
                        detection.append([1] * length)
                        identification.append([drone_name[name]] * length)
                        mode_state.append([drone_name[name] * 3 + drone_mode[mode]] * length)
                        inter.append([interf] * length)
                        
    label.append(inter)
    label.append(detection)
    label.append(identification)
    label.append(mode_state)
    label.append(groups)
    print(mode_state[19])
    
    return label

def labeling_mode() :
    label_mode = []
    
    # detection = []
    # identification = []
    # mode_state = []
    # inter = []
    
    for interf in ["BOTH"] :
        for mode in MODE :
            for name in DRONE_NAME :
                if not (name == 'DIS' and mode == 'HO') :
                    with open(f"{interf}_{name}_{mode}.txt", "r") as fp:
                        length = len(json.load(fp))
                        print(f"    {interf}_{name}_{mode} ...")
                        label_mode.append([drone_mode[mode]] * length)
                        # detection.append([1] * length)
                        # identification.append([drone_name[name]] * length)
                        # mode_state.append([drone_name[name] * 3 + drone_mode[mode]] * length)
                        # inter.append([interf] * length)
                        
    # label.append(inter)
    # label.append(detection)
    # label.append(identification)
    # label.append(mode_state)
    
    # print(mode_state[19])
    
    return label_mode
    