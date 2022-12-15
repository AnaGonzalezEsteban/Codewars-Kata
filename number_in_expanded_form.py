# You will be given a number and you will need to return it as a string in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
# NOTE: All numbers will be whole numbers greater than 0.

# If you liked this kata, check out part 2!!

from enum import *
def expanded_form(num):
    number=str(num)
    list=[]
    for index,element in enumerate(number[::-1]):
        if element!='0':
            element_result=str(int(element)*(10**index))
            list.insert(0,element_result)
    return '+'.join(list)

print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))