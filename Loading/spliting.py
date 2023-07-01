#This is used for DC-CNN model to load preprocessed data

def spliting(input) :
    temp = []
    
    for i in range(int(len(input) / 2)) :
        temp.append(input[0])
        input.pop(0)
        
    res = []

    res.append(temp)
    res.append(input)


    return res