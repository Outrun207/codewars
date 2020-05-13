import re 

def reverse_words(text):
  listWithSpaces=re.split("( )",text[::-1])
  listWithSpaces.reverse()
  stringForReturn = ""
  return stringForReturn.join(listWithSpaces)
