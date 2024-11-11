'''
Description: a python code that calculates the product of all odd numbers between 1 and a given number n
Author:Adars v
Date:11/11/2024

'''


x=int(input("Enter the number:"))
sum=1
i=1
while (i<=x):
    sum=sum*i
    i=i+2
print(sum)    
