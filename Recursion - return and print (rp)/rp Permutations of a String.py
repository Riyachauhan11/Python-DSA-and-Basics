'''
i)Given a string, find and print all the possible permutations of the input string.
ii)Given a string, find and return all the possible permutations of the input string.


Note : The order of permutations are not important. Just print them in different lines.

Sample Input :
abc

Sample Output :
abc
acb
bac
bca
cab
cba'''

#RETURN FUNC
def permutations(string):
    #Implement Your Code Here
    if len(string)==1:
        l=[string]
        return l

    first_char=string[0]
    small_output=permutations(string[1:])
    output=[]

    for ele in small_output:
        new_ele1=first_char+ele
        output.append(new_ele1)
        if len(ele)!=1:
            for i in range(1,len(ele)):
                new_ele2=ele[0:i]+first_char+ele[i:]
                output.append(new_ele2)
        new_ele3=ele+first_char
        output.append(new_ele3)

    return output


string = input()
ans = permutations(string)
for s in ans:
    print(s)



#PRINT FUNC
def permutations(string,ans):
    #Implement Your Code Here
    if len(string)==0:
        for s in ans:
            print(s)
        return 

    first_char=string[0]
    output=[]

    for ele in ans:
        new_ele1=ele+first_char
        output.append(new_ele1)
        if len(ele)!=1:
            for i in range(1,len(ele)):
                new_ele2=ele[0:i]+first_char+ele[i:]
                output.append(new_ele2)
        new_ele3=first_char+ele
        output.append(new_ele3)

    permutations(string[1:],output)


string = input()
permutations(string[1:],[string[0]])

