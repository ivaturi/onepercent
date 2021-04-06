
import re
#! /usr/bin/env python
def is_valid(isbn):
    clean_isbn = isbn.replace("-", "")
    if not re.compile("\\d{9}(\\d|X)$").match(clean_isbn):
        return False
    else:
        nums = list(clean_isbn)
        if nums[-1] is "X":
            nums[-1] = '10' 
        return is_valid_isbn(nums)

def is_valid_isbn(isbn_digits):
    nums = list(map(int, isbn_digits))
    pairwise= zip(nums, range(10, 0, -1))
    return sum([pair[0] * pair[1] for pair in pairwise]) % 11 == 0