li=[]
for i in range(28):
    li.append(int(input()))

li.sort()
an=[]
for i in range(30):
    an.append(i+1)
 
checking=list(set(an)-set(li)) 
checking.sort()
while len(checking)>0:
    print(checking.pop(0))
