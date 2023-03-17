'''A thief robbing a store can carry a maximal weight of W into his knapsack. 
There are N items, and i-th item weigh 'Wi' and the value being 'Vi.' What would be the maximum value V, that the thief can steal?

Input Format :
The first line of the input contains an integer value N, which denotes the total number of items.
The second line of input contains the N number of weights separated by a single space.
The third line of input contains the N number of values separated by a single space.
The fourth line of the input contains an integer value W, which denotes the maximum weight the thief can steal.

Output Format :
Print the maximum value of V that the thief can steal.

Constraints :

1 <= N <= 20
1<= Wi <= 100
1 <= Vi <= 100

Time Limit: 1 sec

Sample Input 1 :

4
1 2 4 5
5 4 8 6
5

Sample Output 1 :

13

Sample Input 2 :

5
12 7 11 8 9
24 13 23 15 16
26

Sample Output 2 :

51'''


from sys import stdin

#RECURSIVE SOLN
def knapsack(weights, values, n, maxWeight,i) :
    #Your code goes here
    if i==n:
        return 0

    if weights[i]<=maxWeight:
        #exclusion of ith item
        ans1=knapsack(weights,values,n,maxWeight,i+1)
        #inclusion of ith item
        ans2=values[i]+knapsack(weights,values,n,maxWeight-weights[i],i+1)
        ans=max(ans1,ans2)
    
    else:
        ans=knapsack(weights,values,n,maxWeight,i+1)

    return ans
  
  
  
#BOTTOM UP APPRAOCH - dp
def knapsackBU(weights, values, n, maxWeight) :
    #Your code goes here
    dp=[[0 for j in range(maxWeight+1)]for i in range(n+1)]

    for i in range(n-1,-1,-1):
        for j in range(0,maxWeight+1):
            if weights[i]<=j:
                ans1=dp[i+1][j]
                ans2=values[i]+dp[i+1][j-weights[i]]
                dp[i][j]=max(ans1,ans2)
            else:
                dp[i][j]=dp[i+1][j]

    return dp[0][maxWeight]
    


def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return weights, values, n, maxWeight


#main
weights, values, n, maxWeight = takeInput()

print(knapsackBU(weights, values, n, maxWeight))

