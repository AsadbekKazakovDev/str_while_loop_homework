def main(s):
    """
    A string of numbers is given. Find the sum of all the digits and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    m = "1234567890"
    i=0
    k=0
    while i<=len(s)-1:
        if s[i] in m:
            k+=int(s[i])
        i+=1
    return k
s = "56786543250"

print(main(s))