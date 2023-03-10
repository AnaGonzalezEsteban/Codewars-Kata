# Introduction
# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

# Task
# Given a year, return the century it is in.

# Examples
# 1705 --> 18
# 1900 --> 19
# 1601 --> 17
# 2000 --> 20

def century(year):
    century=0
    for i in range (0,year,100):
        century+=1
    return century


print(century(1705))
print(century(1900))
print(century(1601))
print(century(2000))
print(century(100))

