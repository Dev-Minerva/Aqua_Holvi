a,b=map(int,input("enter the range:").split())
sum=0
for i in range(a,b):
    if i%2==0:
        sum=sum+i
print("by using for loop")
print("sum of all even numbers between{0} and {1} is: {2}".format(a,b,sum))

sum=0
while a<b:
    if a%2==0:
        sum=sum+a
    a=a+1
print("by using while loop")
print("sum of all the even numbers between {0} and {1} is: {2}".format(a,b,sum))
