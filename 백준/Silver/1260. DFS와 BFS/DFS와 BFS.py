from collections import deque
n,m,v=map(int,input().split())
gra=[[0] * (n+1) for _ in range(n+1)]
visit1=[False]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    gra[a][b]=gra[b][a]=1

    
def dfs(graph,v,visit):
    visit[v]=True
    print(v,end=' ')
    
    for i in range(len(gra[v])):
        if graph[v][i]==1 and not visit[i]:
            dfs(graph,i,visit) 
            
            
visit2=[False]*(n+1)           
def bfs(graph,v,visit):
    queue=deque()
    queue.append(v)
    while queue:
        val=queue.popleft()
        if not visit[val]:
            print(val, end=' ')
            visit[val]=True
            for i in range(len(graph[val])):
                if graph[val][i]== 1 and not visit[i]:
                    queue.append(i)
    
    
                    
dfs(gra,v,visit1)
print()
bfs(gra,v,visit2)
