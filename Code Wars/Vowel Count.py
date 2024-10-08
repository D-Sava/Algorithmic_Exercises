# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels for this Kata (but not y).

# The input string will only consist of lower case letters and/or spaces.

def get_count(sentence):
    
    vowelsCount = 0

    for x in sentence:
        if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
            vowelsCount+=1

    return vowelsCount

print(get_count('Hello'))