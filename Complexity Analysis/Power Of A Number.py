# Time complexity - O(logn)
# Space complexity - O(logn)


def power(x, n):
    # Please add your code here
    if n==0:
        return 1
    small_power=power(x,n//2)
    if n%2==0:
        return small_power*small_power
    else:
        return small_power*small_power*x

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))


''' for a iterative function of power :
    Time complexity - O(n)
    space complexity - O(1)
'''

''' for a recursive function of power :
    Time complexity - O(n)
    space complexity - O(n)
'''

