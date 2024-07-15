from fractions import Fraction

ring=int(input())
li=list(map(int,input().split()))
firstRing=li[0]
for i in range(1,len(li)):
   fra=li[i]*Fraction(1,firstRing)
   print(f'{fra.denominator}/{fra.numerator}')