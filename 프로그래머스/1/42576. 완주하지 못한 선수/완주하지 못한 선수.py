from collections import Counter
def solution(participant, completion):
    part=Counter(participant)
    com=Counter(completion)
    ans=(part-com)
    a=''.join(ans)
    return a