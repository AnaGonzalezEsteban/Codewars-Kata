# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

# What if the string is empty? Then the result should be empty object literal, {}.

def count(string):
    result={}
    for element in string:
        if element not in result:
            result[element]=1
        else:
            result[element]+=1
    return result

print(count('aba'))

#ANSWERS:

# from collections import Counter
# def count(string):
#     return Counter(string)


# def count(string):
#     return {i: string.count(i) for i in string}


# def count(string):
#     letters = {}
#     for c in string:
#         letters[c] = string.count(c)
#     return letters