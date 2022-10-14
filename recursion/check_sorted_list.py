def isSorted(li):
    if len(li)==1 or len(li)==0:
        return True
    if li[0]>li[1]:
        return False
    smaller_list=li[1:]
    return isSorted(smaller_list)
print(isSorted([1,2,3,4,5,7,6]))

#better solution

def isSorted_better(li,si=0):
    if si==len(li)-1 or si==len(li):
        return True
    if li[si]>li[si+1]:
        return False
    is_SmallerPartSorted=isSorted_better(li,si+1)
    return is_SmallerPartSorted
print(isSorted_better([1,2,3,3,4],0))

    