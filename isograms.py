# An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
# Implement a function that determines whether a string that contains only letters is an isogram. 
# Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

# def is_isogram(string):
#     seq=string.lower()
#     seq_list=list(seq)
#     seq_set=set(seq)
#     return len(seq_list)==len(seq_set)

def is_isogram(string):
    lower_string=string.lower()
    return len(list(lower_string))==len(set(lower_string))

print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))

# ANSWERS:
def is_isogram(string):
    return len(string) == len(set(string.lower()))

is_isogram = lambda s: len(set(s.lower())) == len(s)

