a=int(input("Enter a number"))
sum=0
while a>=1:
    b=a%10
    f=1
    for i in range(1,b+1):
        f=f*i
    sum=sum+f
    a=a//10
if sum==a:
    print("Krishnamurthy")
else:
    print("Not Krishnamurthy")
