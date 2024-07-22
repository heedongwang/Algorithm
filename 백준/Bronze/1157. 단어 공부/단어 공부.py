str1=list(input().upper())       
li=sorted(set(str1))
counter=[]

for i in li:
    counter.append(str1.count(i))

if counter.count(max(counter))>=2:
    print("?")
else:
    print(li[counter.index(max(counter))])
