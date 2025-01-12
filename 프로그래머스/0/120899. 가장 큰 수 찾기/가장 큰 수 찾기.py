def solution(array):
    answer = []
    arr = sorted(array)
    answer=[arr[-1],array.index(arr[-1])]

    return answer