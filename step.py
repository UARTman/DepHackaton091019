import numpy, copy

def costyl(a, b):
    for i in a:
        if (b == i).all():
            return False
    return True

def gen(a : numpy.array):
    res=[]
    alt=[]
    for q in a:
        for i in range(a.shape[0]):
            for j in range(a.shape[1]):
                if a[i, j] == 1:
                    if i > 0:
                        if a[i-1, j] == 0:
                            res.append(copy.deepcopy(a))
                            res[-1][i-1, j] = 1
                            if costyl(list(alt), res[-1]):
                                alt.append(res[-1])
                                #alt += gencopy(res[-1])
                            else:
                                res.pop()
                    if i < 14:
                        if a[i+1, j] == 0:
                            res.append(copy.deepcopy(a))
                            res[-1][i+1, j] = 1
                            if costyl(list(alt), res[-1]):
                                alt.append(res[-1])
                                #alt += gencopy(res[-1])
                            else:
                                res.pop()
                    if j > 0:
                        if a[i, j-1] == 0:
                            res.append(copy.deepcopy(a))
                            res[-1][i, j-1] = 1
                            if costyl(list(alt), res[-1]):
                                alt.append(res[-1])
                                #alt += gencopy(res[-1])
                            else:
                                res.pop()
                    if j < 14:
                        if a[i, j+1] == 0:
                            res.append(copy.deepcopy(a))
                            res[-1][i, j+1] = 1
                            if costyl(list(alt), res[-1]):
                                alt.append(res[-1])
                                #alt += gencopy(res[-1])
                            else:
                                res.pop()
    return res