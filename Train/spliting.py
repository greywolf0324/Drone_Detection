# def spliting(input, K) :
#     temp = []
#     tem = []
#     for i in range(int(len(input))) :
#         if (i + 1) % K == 0 :
#             tem.append(input[i])
#             temp.append(tem)    
#             tem = []
#         else :
#             print(i)
#             tem.append(input[i])
    

#     return temp

def spliting(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]
