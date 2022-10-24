'''A child is running up a staircase with N steps, and can hop either 1 step, 2 steps or 3 steps at a time. 
Implement a method to count how many possible ways the child can run up to the stairs. 
You need to return number of possible ways W.'''

def staircase(n):
    if n==0 or n==1:
        return 1
    elif n==2:
        return 2
    x=staircase(n-1)
    y=staircase(n-2)
    z=staircase(n-3)
    return x+y+z
n=int(input())
print(staircase(n))

#the output gets printed in a very similar manner (or recursive tree) as to
#the output we get from recursive function of fibonnaci series
