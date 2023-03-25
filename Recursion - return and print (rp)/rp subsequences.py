
''' i) Given a string (let's say of length n), return all the subsequences of the given string.
    ii)Given a string (lets say of length n), print all the subsequences of the given string.

Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain the same as in the input string.
Note: The order of subsequences are not important.

Sample Input:
abc

Sample Output:
"" (the double quotes just signifies an empty string, don't worry about the quotes)
c 
b 
bc 
a 
ac 
ab 
abc '''

#RETURN FUNC(BOTTOM UP APPROACH)
def subsequences(string):
    #Implement Your Code Here
    if len(string)==0:
        l=[""]
        return l

    smaller_output=subsequences(string[1:])
    for i in range(len(smaller_output)):
        smaller_output.append(string[0]+smaller_output[i])

    return smaller_output


string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)
    
    
#PRINT FUNC(TOP DOWN APPROACH)
def subsequencesPrinted(inpu,outpu):
    if inpu=="":
        print(outpu)
        return

    newinput=inpu[1:]
    newoutput=outpu+inpu[0]

    #dont include 0th char
    subsequencesPrinted(newinput,outpu)

    #include 0th char (in output)
    subsequencesPrinted(newinput,newoutput)

string=input()
subsequencesPrinted(string,"")
