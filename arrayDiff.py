'''
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
It should remove all values from list a, which are present in list b.
'''
def array_diff(a, b):
    li_dif = [i for i in a + b if i not in b] 
    return li_dif
