n=int(input())
che=set()
for i in range(n):
    che.add(input())
che=list(che)
che.sort()
che.sort(key=len)
for i in che:
    print(i)