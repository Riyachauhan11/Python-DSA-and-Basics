'''For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column 
has the largest sum(sum of all the elements in a row/column) amongst all the rows and columns.

Note :
If there are more than one rows/columns with maximum sum, consider the row/column that comes first. 
And if ith row and jth column has the same largest sum, consider the ith row as answer.

Consider :
If there doesn't exist a sum at all then print "row 0 -2147483648", where -2147483648 or -2^31 is the smallest value for the range of Integer.

Input Format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.
Second line onwards, the next 'N' lines or rows represent the ith row values.
Each of the ith row constitutes 'M' column values separated by a single space.

Output Format :
For each test case, If row sum is maximum, then print: "row" <row_index> <row_sum>
OR
If column sum is maximum, then print: "column" <col_index> <col_sum>
It will be printed in a single line separated by a single space between each piece of information.
Output for every test case will be printed in a seperate line.

'''


from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    max_sum_c=-1
    col_index=0
    for j in range(mCols):
        sum=0
        for i in range(nRows):
            sum+=arr[i][j]
        if sum>max_sum_c:
            max_sum_c=sum
            col_index=j
    max_sum_r=-1
    row_index=0
    for i in range(nRows):
        sum=0
        for j in range(mCols):
            sum+=arr[i][j]
        if sum>max_sum_r:
            max_sum_r=sum
            row_index=i
    if max_sum_c>max_sum_r and max_sum_c!=-1 and max_sum_r!=-1:
        print('column',col_index ,max_sum_c)
    elif max_sum_r>=max_sum_c and max_sum_c!=-1 and max_sum_r!=-1:
        print('row',row_index ,max_sum_r)
    if max_sum_r==-1:
        print('row',row_index ,-2147483648)
    
    
#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)

    t -= 1
