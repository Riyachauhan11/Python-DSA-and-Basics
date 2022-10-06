'''For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. 
That is, you need to print in the order followed for every iteration:

a. First row(left to right)
b. Last column(top to bottom)
c. Last row(right to left)
d. First column(bottom to top)

 Mind that every element will be printed only once.
 
Input format :
The first line contains an Integer 't' which denotes the number of test cases or queries to be run. Then the test cases follow.
First line of each test case or query contains two integer values, 'N' and 'M', separated by a single space. They represent the 'rows' and 'columns' respectively, for the two-dimensional array/list.
Second line onwards, the next 'N' lines or rows represent the ith row values.
Each of the ith row constitutes 'M' column values separated by a single space.

Output format :
For each test case, print the elements of the two-dimensional array/list in the spiral form in a single line, separated by a single space.
Output for every test case will be printed in a seperate line.'''



from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    ele_count=0
    total=nRows*mCols
    if nRows%2==0:
        count=nRows//2
    else:
        count=nRows//2+1
    #count indicates the number of spirals to be done.one iteration of for in range of count will print a,b,c,d 
    #one after another and the process will continue like that.
    for k in range(count):
        if ele_count<(total):
            #a
            for i in range(k,mCols-k):
                print(mat[k][i],end=' ')
                ele_count+=1  
        if ele_count<(total):
            #b
            for row in range(1+k,nRows-k):
                print(mat[row][-1-k],end=' ')
                ele_count+=1
        if ele_count<(total):
            #c
            for ele in range(mCols-2-k,-1+k,-1):
                print(mat[nRows-1-k][ele],end=' ')
                ele_count+=1
        if ele_count<(total):
            #d
            for row in range(nRows-2-k,0+k,-1):
                print(mat[row][0+k],end=' ')
                ele_count+=1
   

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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
