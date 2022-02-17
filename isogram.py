from collections import Counter

ASCII_LOWER_BOUND = 97
ASCII_UPPER_BOUND = 123

def is_isogram(string):
    char_counts = Counter(string.lower())
    return all(
        char_counts[char] == 1 
        for char in char_counts 
        if ord(char) in range(ASCII_LOWER_BOUND, ASCII_UPPER_BOUND + 1)
        )





# string = "tutorialspoint"
# ## initializing a list to append all the duplicate characters
# duplicates = []
# for char in string:
#    ## checking whether the character have a duplicate or not
#    ## str.count(char) returns the frequency of a char in the str
#    if string.count(char) > 1:
#    ## appending to the list if it's already not present
#     if char not in duplicates:
#      duplicates.append(char)
# print(*duplicates)
