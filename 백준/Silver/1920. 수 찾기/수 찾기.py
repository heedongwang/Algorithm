import sys
n1=int(input())
li1=set(sys.stdin.readline().split())

n2=int(input())
li2=sys.stdin.readline().split()

for i in li2:
    if i in li1:
        print(1)
    else:
        print(0)