#   *
#  ***
# *****
#*******

n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces<=n-i:
        print(' ',end='')
        spaces+=1
    stars=1
    while stars<=i:
        print('*',end='')
        stars +=1
    count = i-1
    while count >=1:
        print('*',end='')
        count-=1
    print()
    i+=1
 


#  *
# ***
#*****
# ***
#  *

n=int(input())
i=1
n1= (n+1)/2
n2= n1-1
while i<=n1:
    #spaces
    spaces=1
    while spaces <= n1-i:
        print(' ',end='')
        spaces+=1
    #stars
    stars=1
    while stars<= (2*i-1):
        print('*',end='')
        stars+=1
    print()
    i+=1
i=n2
while i>0:
    #spaces
    spaces=1
    while spaces<= n2-i+1:
        print(' ',end='')
        spaces+=1
    #stars
    stars=1
    while stars<=(2*i-1):
        print('*',end='')
        stars+=1
    print()
    i-=1
    


    
    
#isosceles traingle
#    1
#   121  
#  12321
# 1234321

n=int(input())
i=1
while i<=n:
    #spaces
    spaces=1
    while spaces <= n-i:
        print(' ',end='')
        spaces+=1
    #increasing seq
    p=1
    j=1
    while j<=i:
        print(p,end='')
        j+=1
        p+=1
    #decreasing seq
    p=i-1
    while p>=1:
        print(p,end='')
        p-=1
    print()
    i+=1
    
    
    

#    1
#   232
#  34543
# 4567654

n=int(input())
for i in range(1,n+1):
    for spaces in range(n-i):
        print(" ",end='')
    for inc in range(i,2*i,1):
        print(inc,end='')
    for dec in range((2*i)-2,i-1,-1):
        print(dec,end='')
    print()
    
    
    
#   1
#  212
# 32123
#4321234

n=int(input())
i=1
while i<=n:
    #spaces
    spaces=1
    while spaces<=n-i:
        print(' ',end="")
        spaces+=1
    #decreasing seq
    p=i
    count=1
    while count<=i:
        print(p,end='')
        p-=1
        count+=1
    #increasing seq
    k=2
    while k<=i:
        print(k,end='')
        k+=1
    print()
    i+=1
    
   
