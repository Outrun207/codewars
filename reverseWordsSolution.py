'''Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"'''

import re 

def reverse_words(text):
  listWithSpaces=re.split("( )",text[::-1])
  listWithSpaces.reverse()
  stringForReturn = ""
  return stringForReturn.join(listWithSpaces)
