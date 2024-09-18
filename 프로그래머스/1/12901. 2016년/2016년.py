import calendar
def solution(a, b):
    weekday_dict = {0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    answer = weekday_dict[calendar.weekday(2016,a,b)]
    return answer