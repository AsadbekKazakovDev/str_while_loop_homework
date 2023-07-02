def main(s):
    """
    A variable of type str is given. Find how many digits it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    i = 0
    p = 0
    while i<=len(s)-1:
        if s[i].isdigit():
            p+=1
        i+=1
    return p
s = "python 2022"
print(main(s))