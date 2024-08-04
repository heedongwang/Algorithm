from collections import deque
n,m=map(int,input().split())
matrix=[]
for _ in range(n):
    matrix.append(list(map(int,input().split())))

    
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def bfs(matrix,a,b):
    queue=deque()
    queue.append((a,b))
    matrix[a][b]=0
    count=1
    
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nextx=x+dx[i]
            nexty=y+dy[i]
            
            if 0<=nextx<n and 0<=nexty<m:
                if matrix[nextx][nexty]==1:
                    matrix[nextx][nexty]=0
                    queue.append((nextx,nexty))
                    count+=1
    return count

we=[]
for i in range(n):
    for j in range(m):
        if matrix[i][j]==1:
            we.append(bfs(matrix,i,j))


if len(we)==0:
    print(0)
    print(0)
else:
    print(len(we))
    print(max(we))
