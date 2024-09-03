print("sum of even number using for and while loop")
start=int(input("enter the starting value:"))
end=int(input("enter the ending value:"))

sum=0

for x in range(start,end):
 if(x%2==0):
    sum=sum+x
print("sum of even number using for loop is",sum)

sum=0
while(start<end):
    if(start%2==0):
        sum=sum+start
    start=start+1
print("sum of even number using while loop=",sum)    
