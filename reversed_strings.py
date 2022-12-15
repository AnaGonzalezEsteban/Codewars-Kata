# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    word=''
    for i in reversed(list(string)):
        word+=i
    return word

print(solution('string'))