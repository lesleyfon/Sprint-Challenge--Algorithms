'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, index=0, count=0):
    # TBC
    '''
        Psuedocode:
        Step 1: Check the length of the string if it is 0 then we want to immediately return
        Step 2: Add default arguments to represent index and count for keeping track of the current sting at index and count for keeping track of the total number of th we have encountered
        Step 3: check if the letter at index is equal to t and if the string to index plus 1 is equal to h then we have found a match and want to increase count by one
        Step 4: lastly we add a conditional to check if we are at the end of the string, if so we want to return the tonal occurrence of count

    '''
    if len(word) == 0:
        return 0
    if word[index] == 't' and word[index + 1] == 'h':
        count += 1
    index += 1
    if index == (len(word) - 1):
        return count
    return count_th(word, index, count)
    pass


print(count_th(""))
