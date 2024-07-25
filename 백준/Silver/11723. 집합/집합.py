import sys
s=set()
ran=int(input())
for i in range(ran):
    n=sys.stdin.readline().rstrip()
    
    if " " in n:
        a,b=n.split()
        b=int(b)
        if a=="add":
            s.add(b)
        elif a=="remove":
            if b in s:
                s.remove(b)
        elif a=="check":
            if b in s:
                print("1")
            else:
                print("0")
        elif a=="toggle":
            if b not in s:
                s.add(b)
            else:
                s.remove(b)
        
    else:
        a=n
        if a=='all':
            s=set([i for i in range(1, 21)])
        else:
            s=set([])
