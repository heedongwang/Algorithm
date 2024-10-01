from datetime import datetime
from dateutil.relativedelta import relativedelta
def solution(today, terms, privacies):
    termsdic={}
    answer=[]
    todays=datetime.strptime(today,'%Y.%m.%d')
    for i in terms: 
        term,mon=i.split(" ")
        termsdic[term]=int(mon)
        
    for j,p in enumerate(privacies):
        dates,mons=p.split(" ")
        start=datetime.strptime(dates,"%Y.%m.%d")
        end=start+relativedelta(months=termsdic[mons])

        if end<=todays:
            answer.append(j+1)
    return answer