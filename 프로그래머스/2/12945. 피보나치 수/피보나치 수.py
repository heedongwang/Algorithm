def solution(n):
    f0=0
    f1=1
    num=2
    while 2<=num<=n:
        fn = f0 + f1
        f0 = f1
        f1 = fn
        num += 1
    return fn%1234567