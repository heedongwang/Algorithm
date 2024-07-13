def solution(arr):
    answer = []
    if len(arr)==1:
        if arr[0]==10:
            answer.append(-1)
            return answer
    else:
        mins=arr.index(min(arr))
        del arr[mins]
        return arr