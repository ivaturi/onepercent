def is_isogram(string):

    string_lc = string.lower()
    repeat_ok = ['-', ' ']
    char_counts = [string_lc.count(char) > 1  for char in set(string_lc) if char not in repeat_ok]
    return sum(char_counts) == 0 
