# Provided n you have to find out the nth Fibonacci Number. {fibonacci series being - 1, 1, 2, 3, 5, 8, 13, 21,.....}
n=int(input())
a=1
b=1
count=2
if n==1 or n==2:
    print(1)
else:
    while count<n:
        c=a+b
        a=b
        b=c
        count+=1
    print(c)
