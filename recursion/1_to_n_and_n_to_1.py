#printing numbers from 1 to n
#printing numbers from n to 1

def one_to_n(n):
    if n==0:
        return 
    one_to_n(n-1)
    print(n)
    return

def n_to_one(n):
    if n==0:
        return
    print(n)
    n_to_one(n-1)

one_to_n(4)
n_to_one(7)
