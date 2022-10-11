#to print sum of first n natural numbers

def sum_n(n):
    if n==0: #base case
        return 0
    small_output=sum_n(n-1) #hypothesis
    output=small_output+n #induction step
    return output

n=int(input())
print(sum_n(n))

'''simpler soln'''

def sum_n(n):
    if n==0: #base case
        return 0
    return sum_n(n-1)+n

n=int(input())
print(sum_n(n))
