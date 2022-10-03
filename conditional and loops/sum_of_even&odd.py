# Write a program to input an integer n and print the sum of all its even digits and sum of all its odd digits separately.

n=int(input())
sum_of_even=0
sum_of_odd=0
while n>0:
    dig=n%10
    n=n//10
    if dig%2==0:
        sum_of_even+=dig
    else:
        sum_of_odd+=dig
print(sum_of_even, sum_of_odd)
