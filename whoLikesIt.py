'''
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement a function likes :: [String] -> String, which must take in input array, containing the names of people who like an item.
'''

def likes(names):
    if not names:
        return "no one likes this"
        
    elif len(names) >= 4: 
        numbahOfNamez = str(len(names) - 2)
        return ", ".join(names[:2]) + " and " + numbahOfNamez + " others like this"
    
    elif len(names) == 3:
        return ", ".join(names[:2]) + " and " + names[2] + " like this"
    
    elif len(names) == 2:
        return ", ".join(names[:1]) + " and " + names[1] + " like this"

    else:
        return ", ".join(names) + " likes this"
