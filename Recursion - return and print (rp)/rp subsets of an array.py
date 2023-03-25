'''
i)Given an integer array (of length n), find and return all the subsets of input array.
ii)Given an integer array (of length n), find and print all the subsets of input array.

Subsets are of length varying from 0 to n, that contain elements of the array. But the order of elements should remain same as in the input array.


Note : The order of subsets are not important.

Input format :
Line 1 : Size of array

Line 2 : Array elements (separated by space)

Sample Input:
3
15 20 12

Sample Output:
[] (this just represents an empty array, don't worry about the square brackets)
12 
20 
20 12 
15 
15 12 
15 20 
15 20 12'''

#RETURN FUNC
def subset(arr,ans_arr):
    if len(arr)==0:
        ans_arr.append([])
        return ans_arr

    
    first_no=arr[0]
    small_output=subset(arr[1:],ans_arr)
    output=[]

    for ele in small_output:
        output.append(ele)


    for ele in small_output:
        l=[first_no]
        new_ele=l+ele
        output.append(new_ele)

    return output

n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
ans=subset(arr,[])
for i in range(len(ans)):
    len_ele=len(ans[i])
    for j in range(len_ele):
        print(ans[i][j],end=' ')
    print()



#PRINT FUNC
def subset(arr,ans_arr):
    if len(arr)==0:
        for i in range(len(ans_arr)):
            len_ele=len(ans_arr[i])
            for j in range(len_ele):
                print(ans_arr[i][j],end=' ')
            print()
        return

    first_no=arr[0]
    output=[]
    for ele in ans_arr:
        output.append(ele)

    for ele in ans_arr:
        l=[first_no]
        new_ele=ele+l
        output.append(new_ele)

    subset(arr[1:],output)


n=int(input())
arr=list(int(i) for i in input().strip().split(' '))
subset(arr,[[]])

