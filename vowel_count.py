# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    count=0
    vowels='aeiou'
    for character in sentence:
        if character in vowels:
            count+=1
    return count


# ANSWERS:
def getCount(s):
    return sum(c in 'aeiou' for c in s)
    

def getCount(inputStr):
    return sum(inputStr.count(char) for char in ['a', 'e', 'i', 'o', 'u'])