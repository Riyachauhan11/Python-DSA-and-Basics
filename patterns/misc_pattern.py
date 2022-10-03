#Print the following pattern for the given number of rows.

# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321


n=int(input())
i=1
while i<=n:
    #increasing seq
    j=1
    p=1
    while j<=i:
        print(p,end='')
        p+=1
        j+=1
    #spaces
    spaces=1
    while spaces<=(n*2)-(i*2):
        print(' ',end='')
        spaces+=1
    #decreasing seq
    j=1
    p=i
    while j<=i:
        print(p,end='')
        p-=1
        j+=1   
    print()
    i+=1
    
    
    
    
# *000*000*
# 0*00*00*0
# 00*0*0*00
# 000***000

n=int(input())
print('*',end='')
count_0=1
while count_0<=n-1:
    print(0,end='')
    count_0+=1
print('*',end='')
count_0=1
while count_0<=n-1:
    print(0,end='')
    count_0+=1
print('*')
i=2
while i<=n:
    #increasing seq
    j=1
    while j<=i-1:
        print(0,end='')
        j+=1
    print('*',end='')
    #decreasing seq
    j=1
    while j<=n-i:
        print(0,end='')
        j+=1
    print('*',end='')
    #inverted decreasing seq
    j=1
    while j<=n-i:
        print(0,end='')
        j+=1
    print('*',end='')
    #inverted increasing seq
    j=1
    while j<=i-1:
        print(0,end='')
        j+=1
    print()
    i+=1
    
    
# *
# * *
#  * * *
#    * * * *
#  * * *
# * *
# *

n=int(input())
i=1
n1=(n+1)/2
n2=n1-1
while i<=n1:
    #spaces
    spaces=1
    while spaces<=i-1:
        print(' ',end="")
        spaces+=1
    #stars
    stars=1
    while stars<=i:
        print('* ',end="")
        stars+=1
    print()
    i+=1
i=n2
while i>0:
    #spaces
    spaces=1
    while spaces<=i-1:
        print(' ',end="")
        spaces+=1
    #stars
    stars=1
    while stars<=i:
        print('* ',end="")
        stars+=1
    print()
    i-=1
    
    

#5432*
#543*1
#54*21
#5*321
#*4321

n=int(input())
i=1
star_c=n
while i<=n:
    j=1
    p=n
    star=1
    while j<=n:
        if star_c==star:
            print('*',end='')
            j+=1
            p-=1
            star+=1
            continue
        print(p,end='')
        j+=1
        p-=1
        star+=1
    i+=1
    star_c-=1
    print()
