# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    
    newString = ''

    # for x in string_:
    #     if (x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u') or (x != 'A' and x != 'E' or x != 'O' or x != 'U' or x!= 'I'):
    #         newString += x
    
    #alternative
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for x in string_:
        if x in vowels:
            continue
        else:
            newString += x

    return newString