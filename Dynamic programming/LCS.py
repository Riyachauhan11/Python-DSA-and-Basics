'''Given two strings, 'S' and 'T' with lengths 'M' and 'N', find the length of the 'Longest Common Subsequence'.
For a string 'str'(per se) of length K, the subsequences are the strings containing characters 
in the same relative order as they are present in 'str,' but not necessarily contiguous. 
Subsequences contain all the strings of length varying from 0 to K.

Example :
Subsequences of string "abc" are:  ""(empty string), a, b, c, ab, bc, ac, abc.

Input format :
The first line of input contains the string 'S' of length 'M'.
The second line of the input contains the string 'T' of length 'N'.

Output format :
Return the length of the Longest Common Subsequence.

Constraints :

0 <= M <= 10 ^ 3
0 <= N <= 10 ^ 3

Time Limit: 1 sec

Sample Input 1 :

adebc
dcadb

Sample Output 1 :

3

Explanation of the Sample Output 1 :

Both the strings contain a common subsequence 'adb', which is the longest common subsequence with length 3. 

Sample Input 2 :

ab
defg

Sample Output 2 :

0

Explanation of the Sample Output 2 :

The only subsequence that is common to both the given strings is an empty string("") of length 0.'''

from sys import stdin

#ITERATIVE
def lcs(s, t,i,j) :
	#Your code goes here
	n=len(s)
	m=len(t)
	dp=[[-1 for j in range(m+1)]for i in range(n+1)]

	for i in range(n,-1,-1):
		for j in range(m,-1,-1):
			if i==n or j==m:
				dp[i][j]=0

			elif s[i]==t[j]:
				dp[i][j]=1+dp[i+1][j+1]

			elif s[i]!=t[j]:
				ans1=dp[i+1][j]
				ans2=dp[i][j+1]
				dp[i][j]=max(ans1,ans2)

	return dp[0][0]

#RECURSIVE
def lcs(s, t,i,j,dp) :
	#Your code goes here

	if i>=len(s) or j>=len(t):
		return 0

	if s[i]==t[j]:
		if dp[i+1][j+1]==-1:
			smallAns= lcs(s,t,i+1,j+1,dp)
			dp[i+1][j+1]=smallAns
			ans=1+smallAns
		else:
			ans=1+dp[i+1][j+1]

	elif s[i]!=t[j]:
		if dp[i+1][j]==-1:
			ans1=lcs(s,t,i+1,j,dp)
			dp[i+1][j]=ans1
		else:
			ans1=dp[i+1][j]
		
		if dp[i][j+1]==-1:
			ans2=lcs(s,t,i,j+1,dp)
			dp[i][j+1]=ans2
		else:
			ans2=dp[i][j+1]

		ans= max(ans1,ans2)

	return ans

#main ITERATIVE
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())
print(lcs(s, t,0,0))

#main RECURSIVE
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())
n=len(s)
m=len(t)
dp=[[-1 for j in range(m+1)]for i in range(n+1)]
print(lcs(s, t,0,0,dp))

