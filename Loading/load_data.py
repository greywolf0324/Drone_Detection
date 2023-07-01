import json

def load_id_mode(INTERF, DRONE_NAME, MODE) :
    x = []
    
    for interf in ["BOTH"] :
        for name in DRONE_NAME :
            for mode in MODE :
                if not (name == 'DIS' and mode == 'HO') :
                    with open(f"{interf}_{name}_{mode}.txt", "r") as fp:
                        # Load the dictionary from the file
                        
                        print(f"    {interf}_{name}_{mode} ...")
                        x.append(json.load(fp))
                        
    return x

# def load_id(INTERF, DRONE_NAME, MODE) :
#     x = {}
#     for name in DRONE_NAME :
#         x[name] = []
    
#     for interf in ["BOTH"] :
#         for name in DRONE_NAME :
#             for mode in MODE :
#                 if not (name == 'DIS' and mode == 'HO') :
#                     with open(f"{interf}_{name}_{mode}.txt", "r") as fp:
#                         # Load the dictionary from the file
                        
#                         print(f"    {interf}_{name}_{mode} ...")
#                         x[name].append(json.load(fp))
                        
#     return x

def load_mode(INTERF, DRONE_NAME, MODE) :
    x = []
    
    for interf in ["BOTH"] :
        for mode in MODE :
            for name in DRONE_NAME :
                if not (name == 'DIS' and mode == 'HO') :
                    with open(f"{interf}_{name}_{mode}.txt", "r") as fp:
                        # Load the dictionary from the file
                        
                        print(f"    {interf}_{name}_{mode} ...")
                        x.append(json.load(fp))
                        
    return x
