# Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
# No floats or non-positive integers will be passed.

# For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

# [10, 343445353, 3453445, 3453545353453] should return 3453455.


from functools import reduce
def sum_two_smallest_numbers(numbers):
    seq=[min(numbers)]
    numbers.remove(min(seq))
    seq.append(min(numbers))
    return reduce(lambda a,b:a+b,seq)

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))

# ANSWERS:
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2]) 
# sorted()
# sorted()El método clasifica la secuencia dada en orden ascendente o descendente y siempre devuelve una lista ordenada. Este método no afecta la secuencia original.

def sum_two_smallest_numbers(num_list):
    num_list.sort()
    return num_list[0] + num_list[1]
# sort()
# sort()La función es muy similar a sorted() pero a diferencia de sorted, no devuelve nada y realiza cambios en la secuencia original. 
# Además, sort() es un método de clase de lista y solo se puede usar con listas.