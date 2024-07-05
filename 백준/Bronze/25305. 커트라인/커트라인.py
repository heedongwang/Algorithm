n,k= map(int,input().split())


li=list(map(int,input().split()))

li.sort(reverse=True)

cutline=li[k-1]

print(cutline)