# The museum of incredible dull things
# The museum of incredible dull things wants to get rid of some exhibitions. Miriam, the interior architect, comes up with a plan to remove the most boring exhibitions. She gives them a rating, and then removes the one with the lowest rating.

# However, just as she finished rating all exhibitions, she's off to an important fair, so she asks you to write a program that tells her the ratings of the items after one removed the lowest one. Fair enough.

# Task
# Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

# Don't change the order of the elements that are left.

# Examples
# * Input: [1,2,3,4,5], output= [2,3,4,5]
# * Input: [5,3,2,1,4], output = [5,3,2,4]
# * Input: [2,2,1,2,1], output = [2,2,2,1]


def remove_smallest(numbers):
    new_array=numbers
    try:
        new_array.remove(min(new_array))
    except:
        new_array
    return new_array
    # ERROR: You've mutated input list  (expectation assertion is on value of input list, not output of method): [277, 128, 128] should equal [91, 277, 128, 128]

def remove_smallest(numbers):
    new_list=[]
    for index,element in enumerate(numbers):
        if numbers!=[] and index!=numbers.index(min(numbers)):
            new_list.append(element)
    return new_list

print(remove_smallest([1,2,3,4,5]))
print(remove_smallest([5,3,2,1,4]))
print(remove_smallest([2,2,1,2,1]))


# ANSWERS:
def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a

def remove_smallest(numbers):
    copy = numbers.copy()
    if len(copy) > 0: copy.remove(min(copy))
    return copy