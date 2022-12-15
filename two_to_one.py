# Take 2 strings s1 and s2 including only letters from a to z. 
# Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

from functools import reduce
def longest(a1, a2):
    onestr=a1+a2
    onestr=set(onestr)
    onestr=sorted(onestr)
    return reduce(lambda x,y:x+y,onestr)

print(longest("xyaabbbccccdefww","xxxxyyyyabklmopq"))
print(longest("abcdefghijklmnopqrstuvwxyz","abcdefghijklmnopqrstuvwxyz"))
    

# ANSWERS:
def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))