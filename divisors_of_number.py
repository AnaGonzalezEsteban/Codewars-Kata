# Count the number of divisors of a positive integer n.

# Random tests go up to n = 500000.

# Examples (input --> output)
# 4 --> 3 (1, 2, 4)
# 5 --> 2 (1, 5)
# 12 --> 6 (1, 2, 3, 4, 6, 12)
# 30 --> 8 (1, 2, 3, 5, 6, 10, 15, 30)
# Note you should only return a number, the count of divisors. The numbers between parentheses are shown only for you to see which numbers are counted in each case.



def divisors(n):
    counter=0
    for i in range(1,500000):
        if n%i==0:
            counter+=1
    return counter


print(divisors(4))
print(divisors(5))
print(divisors(12))
print(divisors(30))



# ANSWERS:
# For Beginners.

# Time: 11724ms
# it's slow because use isinstance
def divisors5(n):
    return len(list(filter(lambda e: isinstance(e, int), [x if n % x == 0 else None for x in range(1, n + 1)])))


# Time: 7546ms
# it's little fast because just directly check boolean
def divisors4(n):
    return len(list(filter(lambda e: e, [True if n % x == 0 else False for x in range(1, n + 1)])))


# Time: 4731ms
# in python True is evaluate as 1
# so when prime factorization just set True and sum will return count
def divisors3(n):
    return sum([True if n % x == 0 else False for x in range(1, n + 1)])


# Time: 3675ms
# even don't need return true, cause comparison operator will return boolean
def divisors2(n):
    return sum([n % x == 0 for x in range(1, n + 1)])


# same time with above but make short code via lambda expression
divisors = lambda n: sum([n % x == 0 for x in range(1, n + 1)])