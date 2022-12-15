# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.

def as_num(arr):
    # for element in arr:
    #     element=int(element)
    return list(map(lambda x:int(x),arr))

# print(as_num([1,'4','2',3]))

def sum_mix(arr):
    return sum(list(map(lambda x:int(x),arr)))

print(sum_mix([1,'4','2',3]))

#ANSWERS:
def sum_mix(arr):
    return sum(map(int, arr))

def sum_mix(arr):
    return sum(int(n) for n in arr)