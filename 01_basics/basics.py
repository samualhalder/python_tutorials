from math import sqrt
n=int(input("enter a number: "))
cnt=0
if(n==1):
    print("not a prime number")
    exit()
for i in range(1,int(sqrt(n))+1):
    if(n%i==0):
        cnt+=1
        if(n//i!=i):
            cnt+=1
if cnt==2:
    print("its a prime number")
else:
    print("not a prime number")
