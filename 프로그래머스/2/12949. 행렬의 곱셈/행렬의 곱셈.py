
def solution(arr1, arr2):
    answer=[]
    
    for i in range(len(arr1)):
        arr=arr1[i]
        row=[]
        for j in range(len(arr2[0])):
            cnt=0
            for k in range(len(arr2)):
                cnt+=arr[k]*arr2[k][j]
            row.append(cnt)
        answer.append(row)
            
        
            
    return answer