person=0
maxperson=[]

while True:
    a,b= map(int,input().split())
    person=person-a+b
    maxperson.append(person)
    if len(maxperson)==10:
        break
    
print(max(maxperson))