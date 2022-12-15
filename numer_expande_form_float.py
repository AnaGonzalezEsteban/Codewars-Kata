# Write Number in Expanded Form - Part 2
# This is version 2 of my 'Write Number in Exanded Form' Kata.

# You will be given a number and you will need to return it as a string in expanded form.

# For example:

# expanded_from(807.304); // Should return "800 + 7 + 3/10 + 4/1000"
# expanded_from(1.24); // should return "1 + 2/10 + 4/100"
# expanded_from(7.304); // should return "7 + 3/10 + 4/1000"
# expanded_from(0.04); // should return "4/100"


def expanded_form(num):
    number=str(num).split('.')
    integer_number=number[0]
    float_number=number[1]
    integer_list=[]
    float_list=[]
    for index,element in enumerate(integer_number[::-1]):
        if element!='0':
            element_result=str(int(element)*(10**index))
            integer_list.insert(0,element_result)
    for index,element in enumerate(float_number):
        if element!='0':
            element_result=str(int(element))+'/'+str((10**(index+1)))
            float_list.append(element_result)
    integer_join=' + '.join(integer_list)
    float_join=' + '.join(float_list)
    return integer_join + ' + ' + float_join if len(integer_join)>=1 else float_join


print(expanded_form(807.304))
print(expanded_form(1.24))
print(expanded_form(7.304))
print(expanded_form(0.04))
