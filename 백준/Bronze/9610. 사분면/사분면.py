num=int(input())
q1,q2,q3,q4,axis=0,0,0,0,0
count=0
while num>count:
    x,y=map(int,input().split())
    if x>0 and y>0:
        q1+=1
    elif x<0 and y>0:
        q2+=1
    elif x<0 and y<0:
        q3+=1
    elif x>0 and y<0:
        q4+=1
    elif x==0 or y==0:
        axis+=1
    count+=1
print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')
print(f'Q4: {q4}')
print(f'AXIS: {axis}')