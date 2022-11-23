'''Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
Return true or false.
Do it recursively.
E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.'''


def contains(s, t):
    # Implement This Function Here
    if len(t)==0:
        return True
    elif len(s) == 0 and len(t)> 0:
        return False
    if s[0] == t[0]:
        return contains(s[1:], t[1:])
    else:
        return contains(s[1:], t)


s = input()
t = input()

ans = contains(s, t)
if ans is True:
    print('true')
else:
    print('false')
