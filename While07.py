def main(s):
    """
    A string of numbers is given. Find how many even digits there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    m = "24680"
    i=0
    k=0
    while i<=len(s)-1:
        if s[i] in m:
            k+=1
        i+=1
    return k
s = "56786543250"

print(main(s))