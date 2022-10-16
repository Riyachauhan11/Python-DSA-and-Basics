def binary_search(arr,x,si,ei):
    if si>ei:
        return -1

    mid=(si+ei)//2
    if arr[mid]==x:
        return mid
    elif arr[mid]>x:
        return binary_search(arr,x,si,mid-1)
    else:
        return binary_search(arr,x,mid+1,ei)

print(binary_search([1,2,3,4,5,6,7],9,0,6))
