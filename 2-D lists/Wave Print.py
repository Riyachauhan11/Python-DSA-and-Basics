'''For a given two-dimensional integer array/list of size (N x M), print the array/list in a sine wave order, 
i.e, print the first column top to bottom, next column bottom to top and so on.

Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.
Second line onwards, the next 'N' lines or rows represent the ith row values.
Each of the ith row constitutes 'M' column values separated by a single space.

Output format :
For each test case, print the elements of the two-dimensional array/list in the sine wave order in a single line, separated by a single space.
Output for every test case will be printed in a seperate line.'''

def wavePrint(mat, nRows, mCols):
    #Your code goes here
    row=0
    for j in range(mCols):
        for i in range(nRows):
            print(mat[row][j],end=' ')
            if j%2==0 and i<=nRows-2:
                row+=1
                #print(row)
            elif j%2!=0 and i<=nRows-2:
                row-=1
    print()

t=int(input())
for i in range(t):
    str=input().split()
    n,m=int(str[0]),int(str[1])
    li=[[int(j) for j in input().split()] for i in range(n)]
    wavePrint(li, n, m)
