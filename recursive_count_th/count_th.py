'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, index=0, count=0):
    # TBC
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
