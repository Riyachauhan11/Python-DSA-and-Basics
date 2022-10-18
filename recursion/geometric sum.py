# Given k, find the geometric sum i.e.
# 1 + 1/2 + 1/4 + 1/8 + ... + 1/(2^k) 

# Sample Input 1 :
# 3
# Sample Output 1 :
# 1.87500

# Explanation for Sample Input 1:
# 1+ 1/(2^1) + 1/(2^2) + 1/(2^3) = 1.87500

def geometric_sum(k):
    if k==0:
        return 1
    return (1/(2**k))+geometric_sum(k-1)

k=int(input())
value=geometric_sum(k)
print('%.5f' % value) #ans will be printed upto 5 decimal places


