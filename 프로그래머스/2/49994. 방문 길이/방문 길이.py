def solution(dirs):
    x, y= 0, 0
    paths = {'U':[0,1], 'D':[0,-1], 'L':[-1,0], 'R':[1,0]}
    boxes=set()
    for i in dirs:
        dx = x + paths[i][0]
        dy = y + paths[i][1]
        if -5 <= dx <= 5 and -5 <= dy <= 5:
            boxes.add((x,y,dx,dy))
            boxes.add((dx,dy,x,y))
            x, y = dx, dy
    # print(boxes)
    path_len=len(boxes)/2
    return path_len