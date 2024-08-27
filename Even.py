a,b=map(int,input("Enter The range").split())

#by using For loop
sum=0
for i in range(a,b):
    if i%2==0:
        sum=sum+i
print("By using For Loop")
print("Sum Of All the Even Numbers Between {0} and {1} is:{2}".format(a,b,sum))


#by using While loop
sum=0
while a<b:
    if a%2==0:
        sum=sum+a
    a=a+1
print("By using While Loop")
print("Sum of all the Even Numbers Between {0} and {1} is:{2}".format(a,b,sum))
