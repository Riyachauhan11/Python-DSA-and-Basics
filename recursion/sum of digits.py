# Write a recursive function that returns the sum of the digits of a given integer.

def sum_of_digits(n):
    if n==0:
        return 0
    return n%10+sum_of_digits(n//10)

n=int(input())
sum=sum_of_digits(n)
print(sum)
