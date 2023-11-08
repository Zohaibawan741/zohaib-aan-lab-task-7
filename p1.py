a=int(input("entre a deviser"))
b=int(input("entre a devident"))

quotient=0
while a<=b:
     b-=a
     quotient+=1

print(quotient)  