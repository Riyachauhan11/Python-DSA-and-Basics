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
    
 


#4444
#333
#22
#1

n=int(input())
i=1
count=n
while i<=n:
    j=1
    while j<=count:
        print(count,end='')
        j+=1
    print()
    i+=1
    count-=1 
    

    
    
#    1
#   12 
#  123
# 1234

n=int(input())
i=1
while i<=n:
    spaces=1
    while spaces <= n-i :
        print(' ',end='')
        spaces +=1
    j=1
    while j<=i:
        print(j,end='')
        j+=1
    print()
    i+=1
