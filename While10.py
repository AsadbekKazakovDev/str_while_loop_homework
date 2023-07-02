def main(s):
    """
    A string of numbers is given. Find and return the sum of all odd digits.
    Args:
        s: str
    Returns:
        int: return answer
    """
    m = "24680"
    i=0
    k=0
    while i<=len(s)-1:
        if s[i] not in m:
            k+=int(s[i])
        i+=1
    return k
s = "56786543250"

print(main(s))