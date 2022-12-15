# Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

# Examples
# "This is an example!" ==> "sihT si na !elpmaxe"
# "double  spaces"      ==> "elbuod  secaps"



# def concat_all(strings):
#     """Recibe una lista de cadenas y las reduce a una sola concatenandolas"""
#     total_so_far=''
#     for element in strings:
#         total_so_far = total_so_far + ' ' + element  # + se aplica a las cadenas para concatenar
#     return total_so_far


# def reverse_words(text):
#     text=text.split()
#     new_list=[]
#     new_text=''
#     for word in text:
#         new_word=word[::-1]
#         new_list.append(new_word)
#     new_text=concat_all(new_list)
#     return new_text
# print(reverse_words('hola mundo!'))

# from operator import concat
# from functools import reduce
# def reverse_words(text):
#     text=text.replace(' ',' ,')
#     text=text.split(',')
#     new_list=[]
#     new_text=''
#     for word in text:
#         new_word=word[::-1]
#         new_list.append(new_word)
#     new_text=reduce(concat,new_list)
#     new_text.strip()
#     return new_text


def reverse_words(str):
  strList = []
  for word in str.split(' '):
      strList.append(word[::-1])
  return ' '.join(strList)


print(reverse_words('The quick brown fox jumps over the lazy dog.'))
print(reverse_words('apple'))
print(reverse_words('a b c d'))
print(reverse_words('double  spaced  words'))



# def reverse_words(text):
#     return text[::-1]

# print(reverse_words('hola mundo!'))

# reverse_words_=lambda x: x[::-1]
# print(reverse_words_('hola mundo!'))

# cadena='hola'
# print(cadena[-1])
# print(cadena[-len(cadena)])
# print(cadena[::-1])

#ANSWERS:
def reverse_words(str):
  return " ".join(map(lambda word: word[::-1], str.split(' ')))

def reverse_words(str):
  return ' '.join([i[::-1] for i in str.split(' ')])