def solution(num_list):
    add,mul=0,1
    for i in num_list:
        add+=i
        mul*=i
    twice=add**2
    if mul<=twice:
        return 1
    else:
        return 0