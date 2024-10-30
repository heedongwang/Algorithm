def DFS(matrix,v,visited):
    visited[v]=True
    for i in range(len(matrix[v])):
        if matrix[v][i]==1 and not visited[i]:
            DFS(matrix,i,visited)

def solution(n, computers):
    answer=0
    result=list()
    visited=[False]*(len(computers))

    
    for i in range(n):
        if not visited[i]:
            DFS(computers,i,visited)
            answer+=1
    

    return answer