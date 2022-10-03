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

    
    
    
#1
#12
#123
#1234

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
    

       
