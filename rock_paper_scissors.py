
def rps(p1, p2):

    result=p2

    if p1=='rock' and p2=='paper':
        result= f'Player {2} won!'
    elif p1=='paper' and p2=='scissors':
        result= f'Player {2} won!'
    elif p1=='scissors' and p2=='rock':
        result=f'Player {2} won!'
    elif p2=='rock' and p1=='paper':
        result= f'Player {1} won!'
    elif p2=='paper' and p1=='scissors':
        result= f'Player {1} won!'
    elif p2=='scissors' and p1=='rock':
        result=f'Player {1} won!'
    else:
        result='Draw!'

    return result


print(rps('rock','paper'))
print(rps('paper','rock'))
print(rps('paper','paper'))
    




