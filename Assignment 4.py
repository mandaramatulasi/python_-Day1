# WAP to find factorial of a given number
num=int(input("enter a number:"))

sum=1

i=1

while (i<=num):
    sum=sum*i
    i=i+1

print("the factorial is:",sum)