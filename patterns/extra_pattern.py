#Print the following pattern for the given number of rows.

#1111
#000
#11
#0

n=int(input())
a=False
p=n
for i in range(1,n+1,1):
    if a:
        a=False
    else:
        a=True
    for j in range(p,0,-1):
        print(int(a),end='')
    p-=1
    print()
    

    

# 123456
#  23456
#   3456
#    456
#     56
#      6
#     56
#    456
#   3456
#  23456
# 123456

n=int(input())
p=n
for i in range(1,n+1):
    for s in range(i-1):
        print(' ',end='')
    for j in range(p,0,-1):
        print(i,end='')
        i+=1
    p-=1
    print()
p=n-2
for i in range(1,n):
    k=n
    k-=i
    #print(i,k)
    for s in range(p,0,-1):
        print(' ',end='')
    for j in range(1,i+2):
        print(k,end='')
        k+=1
    p-=1
    print()

    
  
#4444444
#4333334
#4322234
#4321234
#4322234
#4333334  
#4444444

n=int(input())
count=n*2-3
n1=int((n+1)/2)
t=n-1
o=n
for i in range(1):
    for j in range((2*n)-1):
        print(n,end='')
    print()
i=1
while i<=n-1:
    #inc seq
    k=n
    j=1
    while j<=i:
        print(k,end='')
        k-=1
        j+=1
    #same nos
    j=1
    while j<=count:
        print(t,end='')
        j+=1
    #inc seq
    j=1
    while j<=i:
        print(o,end='')
        o+=1
        j+=1
    print()
    o=n-i
    i+=1
    t-=1
    count-=2
i=1
r=n-1
count=1
t=2
while i<=n-1:
    #dec seq
    o=n
    j=1
    while j<=r:
        print(o,end='')
        o-=1
        j+=1
    #same nos
    j=1
    while j<=count:
        print(t,end='')
        j+=1
    #dec seq
    j=1
    q=i+1
    while j<=r:
        print(q,end='')
        q+=1
        j+=1
    print()
    count+=2
    i+=1
    r-=1
    t+=1

    
    
    
#1    2   3    4   5
#11   12  13   14  15
#21   22  23   24  25
#16   17  18   19  20
#6    7    8   9   10


n=int(input())
p=1
if n%2==0:
    n1=int((n+1)/2)+1
else:
    n1=int((n+1)/2)
for i in range(1,n1+1):
    for j in range(1,n+1):
        if j==1:
            first=p
        print(p,end=' ')
        p+=1
    print()
    if n%2==0 and i==int(n/2):
        first = first+n
        p=first
        continue
    first=first+(n*2)
    p=first
if n%2!=0:
    p=p-n*3
    n1=int((n+1)/2)-1
else:
    p=p-n*4
    n1=int(n/2)-1
for i in range(1,n1+1):
    for j in range(1,n+1):
        if j==1:
            first=p
        print(p,end=' ')
        p+=1
    print()
    first=first-(n*2)
    p=first
