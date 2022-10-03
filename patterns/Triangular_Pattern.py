#*
#**
#***
#****

n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print('*',end='')
        j+=1
    print()
    i+=1
    
    
    
#1
#22
#333
#4444

n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(i,end='')
        j+=1
    print()
    i+=1

    
    
    
# 1
# 12
# 123
# 1234

n=int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        print(j,end="")
        j+=1
    print()
    i+=1
    
    
    
#1
#21
#321
#4321

n=int(input())
i=1
while i<=n:
    j=1
    k=i
    while j<=i:
        print(k,end='')
        j+=1
        k-=1
    print()
    i+=1

    
    

# 1
# 23
# 345
# 4567

n=int(input())
i=1
while i<=n:
    j=1
    k=i
    while j<=i:
        print(k,end='')
        k+=1
        j+=1
    print()
    i+=1
    
    
    

# 1
# 23
# 456
# 78910

n=int(input())
i=1
p=1
while i<=n:
    j=1
    while j<=i:
        print(p,end='')
        j+=1
        p+=1
    print()
    i+=1
  
  
  
#1
#11
#202
#3003

n=int(input())
i=1
if n>=1:
    print(1)
    while i<=(n-1):
        count_of_0=0
        print(i,end='')
        while count_of_0 < (i-1):
            print(0,end='')
            count_of_0+=1
        print(i,end='')
        print()
        i+=1
        
#1
#11
#121
#1221
n=int(input())
i=1
if n>=1:
    print(1)
    while i<=(n-1):
        count_of_2=0
        print(1,end='')
        while count_of_2 < (i-1):
            print(2,end='')
            count_of_2+=1
        print(1,end='')
        print()
        i+=1
    
    
#1234
#123
#12
#1

n=int(input())
i=1
count=n
while i<=n:
    j=1
    while j<=count:
        print(j,end='')
        j+=1
    print()
    i+=1
    count-=1
    

 #A
 #BB
 #CCC

n=int(input())
i=1
start_char=ord('A')
while i<=n:
    j=1
    while j<=i:
        print(chr(start_char),end='')
        j+=1
    print()
    start_char+=1
    i+=1

    
#A
#BC
#CDE
#DEFG

n=int(input())
i=1
while i<=n:
    j=1
    start_char=chr(ord('A')+i-1)
    while j<=i:
        print(chr(ord(start_char)+j-1),end='')
        j+=1
    print()
    i+=1
    

    
    
#E
#DE
#CDE
#BCDE
#ABCDE

n=int(input())
i=1
while i<=n:
    j=1
    needed_char=chr(ord('A')+n-1)
    start_char=chr(ord(needed_char)-i+1)
    while j<=i:
        print(chr(ord(start_char)+j-1),end='')
        j+=1
    print()
    i+=1



    

#inverted triangle (2 methods)
# ****
# ***
# **
# *

n=int(input())
i=1
count = n
while i<=n:
    j=1
    while j<=count:
        print('*',end='')
        j+=1
    print()
    i+=1
    count-=1

n=int(input())
i=1
while i<=n:
    j=1
    while j<=(n-i+1):
        print('*',end='')
        j+=1
    print()
    i+=1
    
    
    

# reversed triangle pattern
#    *
#   **   
#  ***
# ****

n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces <= n-i:
        print(' ',end='')
        spaces+=1
    stars=1
    while stars <= i:
        print('*',end='')
        stars+=1
    print()
    i+=1
    
    
    

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
