from collections import defaultdict

L = [1,2,45,55,5,4,4,4,4,4,4,5456,56,6,7,67]

def max_occur(L) :
    d = defaultdict(int)
    for i in L:
        d[i] += 1
    result = max(d.items(), key=lambda x: x[1])

    return result[0]