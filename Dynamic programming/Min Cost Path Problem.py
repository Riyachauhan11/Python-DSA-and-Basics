'''An integer matrix of size (M x N) has been given. Find out the minimum cost to reach from the cell (0, 0) to (M - 1, N - 1).
From a cell (i, j), you can move in three directions:

1. ((i + 1),  j) which is, "down"
2. (i, (j + 1)) which is, "to the right"
3. ((i+1), (j+1)) which is, "to the diagonal"

The cost of a path is defined as the sum of each cell's values through which the route passes.

Input format :
The first line of the test case contains two integer values, 'M' and 'N', separated by a single space. 
They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.

The second line onwards, the next 'M' lines or rows represent the ith row values.

Each of the ith row constitutes 'N' column values separated by a single space.

Output format :
Print the minimum cost to reach the destination.

Constraints :

1 <= M <= 10 ^ 2
1 <= N <=  10 ^ 2

Time Limit: 1 sec

Sample Input 1 :

3 4
3 4 1 2
2 1 8 9
4 7 8 1

Sample Output 1 :

13

Sample Input 2 :

3 4
10 6 9 0
-23 8 9 90
-200 0 89 200

Sample Output 2 :

76

Sample Input 3 :

5 6
9 6 0 12 90 1
2 7 8 5 78 6
1 6 0 5 10 -4 
9 6 2 -10 7 4
10 -2 0 5 5 7

Sample Output 3 :

18'''

import sys
from sys import stdin
MAX_VALUE = 2147483647

# RECURSIVELY
def minCost(cost,i,j,n,m):
    #Special Case
    if i==n-1 and j==m-1:
        return cost[i][j]
    #Base case
    if i>=n or j>=m:
        return sys.maxsize
    
    ans1=minCost(cost,i,j+1,n,m)
    ans2=minCost(cost,i+1,j,n,m)
    ans3=minCost(cost,i+1,j+1,n,m)
    
    ans=cost[i][j]+min(ans1,ans2,ans3)
    return ans



# USING DP AND RECURSIVELY
def minCostPath(mat,i,j, mRows, nCols,dp) :
	#Your code goes here
    #Special case
    if i==mRows-1 and j==nCols-1:
        return mat[i][j]

    #Base case
    if i==mRows or j==nCols:
        return sys.maxsize

    if dp[i+1][j]==sys.maxsize:
        ans1=minCostPath(mat,i+1,j,mRows,nCols,dp)
        dp[i+1][j]=ans1
    else:
        ans1=dp[i+1][j]

    if dp[i][j+1]==sys.maxsize:
        ans2=minCostPath(mat,i,j+1,mRows,nCols,dp)
        dp[i][j+1]=ans2
    else:
        ans2=dp[i][j+1]

    if dp[i+1][j+1]==sys.maxsize:
        ans3=minCostPath(mat,i+1,j+1,mRows,nCols,dp)
        dp[i+1][j+1]=ans3
    else:
        ans3=dp[i+1][j+1]

    minCost=mat[i][j] + min(ans1,ans2,ans3)
   
    return minCost

  
# USING DP AND ITERATIVELY (BOTTOM UP APPROACH)
 def minCostPathBU(mat, mRows, nCols,i,j) :
	#Your code goes here
    dp=[[MAX_VALUE for j in range(nCols+1)]for i in range(mRows+1)]
    for i in range(mRows-1,-1,-1):
        for j in range(nCols-1,-1,-1):
            if i==mRows-1 and j==nCols-1:
                dp[i][j]=mat[i][j]
            else:
                dp[i][j]=mat[i][j]+min(dp[i+1][j],dp[i][j+1],dp[i+1][j+1])


    return dp[0][0]


# USING DP AND ITERATIVELY (TOP DOWN APPROACH) (i and j taken 0 in both approaches)
def minCostPathTD(mat, mRows, nCols,i,j) :
	#Your code goes here
    dp=[[MAX_VALUE for j in range(nCols+1)]for i in range(mRows+1)]
    for i in range(1,mRows+1):
        for j in range(1,nCols+1):
            if i==1 and j==1:
                dp[i][j]=mat[0][0]
            else:
                dp[i][j]=mat[i-1][j-1]+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])


    return dp[mRows][nCols]




#taking input using fast I/O method
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    mRows = int(li[0])
    nCols = int(li[1])
    
    if mRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(mRows)]
    return mat, mRows, nCols


#main
mat, mRows, nCols = take2DInput()
dp=[[sys.maxsize for j in range(nCols+1)]for i in range(mRows+1)] ''' for USING DP AND RECURSIVELY'''
#creating dp one size bigger in both row and column to avoid index error in function
#for eg while calling j+1 in some cases it will return our base case which would only be possible with the dp we r using
print(minCostPath(mat,0,0, mRows, nCols,dp))

#main
mat, mRows, nCols = take2DInput()
print(minCostPathTD(mat, mRows, nCols,0,0))


