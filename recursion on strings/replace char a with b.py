#replacing one character of string with another character recursively

'''no starting index approach is used here since we have to create multiple strings here to solve the question
as we cant make changes within the original string itself as strings are immutable.'''

def replace_char(s,a,b):
    if len(s)==0:
        return s
    small_output=replace_char(s[1:],a,b)
    if s[0]==a:
        return b+small_output
    else:
        return s[0]+small_output

print(replace_char('soon','o','e'))
