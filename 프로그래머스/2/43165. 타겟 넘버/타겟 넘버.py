def solution(numbers, target):
    global count 
    count= 0
    def dfs(i,total):
        global count
        if i==len(numbers):
            if total==target:
                count+=1
            return
        dfs(i+1,total+numbers[i])
        dfs(i+1,total-numbers[i])
        return
    dfs(0,0)
    return count