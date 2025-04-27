def reverse_string(s):
    # the string is empty or has 1 character - base case
    if len(s) <= 1:
        return s
    # last character + call recursive with remaining string 
    return s[-1] + reverse_string(s[:-1])