import numpy as np
def solution(sizes):
    answer = 0
    for i in range(len(sizes)):
        if sizes[i][0]<sizes[i][1]:
            sizes[i][0],sizes[i][1]=sizes[i][1],sizes[i][0]
    col1,col2= map(int,np.max(sizes, axis=0))

    return col1*col2