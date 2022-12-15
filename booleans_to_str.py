# Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.

def bool_to_word(boolean):
    if boolean:
        return 'Yes'
    else:
        return 'No'

print(bool_to_word(True))
print(bool_to_word(False))

print(bool_to_word(4%2==0))
print(bool_to_word(5%2==0))


# ANSWERS

# def bool_to_word(bool):
#     return "Yes" if bool else "No"


# def bool_to_word(bool):
#     return ['No', 'Yes'][bool]


# bool_to_word = lambda b: b and "Yes" or "No"


# bool_to_word = {True: 'Yes', False: 'No'}.get