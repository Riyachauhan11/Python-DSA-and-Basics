'''Write a program to do basic string compression. For a character which is consecutively repeated more than once, 
replace consecutive duplicate occurrences with the count of repetitions.

Example:
If a string has 'x' repeated 5 times, replace this "xxxxx" with "x5".
The string is compressed only when the repeated character count is more than 1.

Note:
Consecutive count of every character in the input string is less than or equal to 9.'''



from sys import stdin
def getCompressedString(string) :
	# Write your code here.
        new_str=''
        i=0
        length=len(string)
        while i<=length-1:
            count=1
            for j in range(i+1,length):
                if string[i]==string[j]:
                    i+=1
                    count+=1
                else:
                    break
            if count>1:
                new_str+=string[i]+str(count)
            else:
                new_str+=string[i]
            i+=1
        return new_str  

# Main.
string = stdin.readline().strip();
ans = getCompressedString(string)
print(ans)
