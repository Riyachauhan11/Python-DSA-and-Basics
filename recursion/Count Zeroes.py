'''Given an integer N, count and return the number of zeros that are present in the given integer using recursion.
in case numbers like 00010204 are used as input then the output will be 2 because when you convert it to an integer, it becomes 10204.'''

def count_zeroes(n):
    if n==0:
        return 1
    if n//10==0:
        return 0
    if n%10==0:
        return 1+count_zeroes(n//10)
    else:
        return count_zeroes(n//10)
        
n=int(input())
count=count_zeroes(n)
string=str(n)
lis=[]
for i in string:
    lis.append(i)
start_zeroes=0
if lis[0]=='0' and len(lis)>1:
    for i in range(0,len(lis)):
        if lis[i]==0 and lis[i+1]!=0:
            start_zeroes+=1
            break
        else:
            start_zeroes+=1
print(count-start_zeroes)
            
