'''Given an integer array A of size N, check if the input array can be splitted in two parts such that -

- Sum of both parts is equal
- All elements in the input, which are divisible by 5 should be in same group.
- All elements in the input, which are divisible by 3 (but not divisible by 5) should be in other group.
- Elements which are neither divisible by 5 nor by 3, can be put in any group.

Groups can be made with any set of elements, i.e. elements need not to be continuous. And you need to consider each and every element of input array in some group.
Return true, if array can be split according to the above rules, else return false.'''


def split(arr, n, i, lsum, rsum):
    if n == i:
        return lsum == rsum
    if (arr[i] % 5 == 0):
        lsum += arr[i]
    elif (arr[i] % 3 == 0):
        rsum += arr[i]
    else:
        return (split(arr, n, i+1, lsum, rsum+arr[i])) or (split(arr, n, i+1, lsum+arr[i], rsum))
    # For cases when element is multiple of 3 or 5.
    return split(arr, n, i+1, lsum, rsum)


def split_array(arr, n):
    return split(arr, n, 0, 0, 0)


n = int(input())
arr = list([int(ele) for ele in input().split()])

if (split_array(arr, n)):
    print("true")
else:
    print("false")
