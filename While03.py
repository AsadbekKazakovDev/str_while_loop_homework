import string
def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    count = 0
    i = 0
    while i <= len(s)-1:
         
        if s[i].isupper():
            
            count +=1
        i+= 1
    return count
s = "CodeschoolUz"
print(main(s))