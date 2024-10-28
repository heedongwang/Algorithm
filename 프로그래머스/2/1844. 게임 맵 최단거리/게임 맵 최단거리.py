from collections import deque

def solution(maps):

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    result = 0

    col = len(maps)
    row = len(maps[0])

    check = [[0]*row for _ in range(col)]
    dis = [[0]*row for _ in range(col)]
    queue = deque()

    check[0][0] = 1
    dis[0][0] = 1
    queue.append((0,0))

    while queue:
        now = queue.popleft()

        for i in range(4):
            x = now[0]+dx[i]
            y = now[1]+dy[i]

            if 0<=x<=col-1 and 0<=y<=row-1:
                if check[x][y] == 0 and maps[x][y] == 1:
                    check[x][y] = 1
                    dis[x][y] = dis[now[0]][now[1]] + 1
                    queue.append((x,y))

    result = -1 if dis[col-1][row-1] == 0 else dis[col-1][row-1]

    return result