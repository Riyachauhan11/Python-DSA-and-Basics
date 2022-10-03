#Write a program to generate the reverse of a given number n.
n=int(input())
rev=0
while n>0:
    dig=n%10
    n=n//10
    rev=rev*10+dig
print(rev)
