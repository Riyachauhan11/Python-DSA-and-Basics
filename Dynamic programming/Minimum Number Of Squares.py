'''A number can always be represented as a sum of squares of other numbers. 
Note that 1 is a square and we can always break a number as [(1 * 1) + (1 * 1) + (1 * 1) + …]. 
Given a number n, find the minimum number of squares that sum to n.

Input format:
The first and only line of input contains an integer N (1 <= N <= 10000)

Constraints:
Time Limit: 1 seconds

Output format:

The first and only line of output contains the minimum number if squares that sum to n.

Sample Test Cases:

Sample Input 1:

100

Sample Output 1:

1

Explanation:

We can write 100 as 10^2 also, 100 can be written as (5^2) + (5^2) + (5^2) + (5^2), 
but this representation requires 4 squares. So, in this case, the expected answer would be 1, that is, 10^2.'''


import sys
from sys import stdin
from sys import maxsize 
from sys import setrecursionlimit
setrecursionlimit(10**6)


def minStepsTo1(n,dp):
    #Implement Your Code Here
    if n==0:
        return 0
    
    i=1
    ans=sys.maxsize
    while i*i <= n:
        newCheckValue=n-(i**2)
        if dp[newCheckValue]==-1:
            val_at_index=minStepsTo1(newCheckValue,dp)
            curr_ans=1+val_at_index
            dp[newCheckValue]=val_at_index
        else:
            curr_ans=dp[newCheckValue]+1

        ans=min(curr_ans,ans)
    
        i+=1
    return ans

def minStepsTo1I(n):
    dp=[-1 for i in range(n+1)]
    dp[0]=0
    i=1
    while i<=n:
        j=1
        ans=sys.maxsize

        while j*j<=i:
            curr_ans=1+dp[i-(j*j)]
            ans=min(curr_ans,ans)
            j+=1
        
        dp[i]=ans        
        i+=1

    return dp[n]

    
n = int(input())
dp=[-1 for i in range(n+1)]
ans = minStepsTo1I(n)
print(ans)







