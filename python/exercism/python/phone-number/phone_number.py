#! /usr/bin/env python

import re
from string import digits
class PhoneNumber:
    def __init__(self, number):
        nums = "".join(i for i in number if i.isdigit())
        # Raise an error if there are insufficient digits
        if len(nums) > 11 or len(nums) < 9 or len(nums) is 11 and nums[0] is not "1":
            raise ValueError("Insufficient digits: You probably entered an invalid number.")

        pattern = re.compile(r'1?([2-9]\d{2})([2-9]\d{2})(\d{4})')
        
        matches = pattern.findall(nums)

        if not matches:
            raise ValueError("Incorrect phone number format!")

        pnr = list(matches[0])
        self.number = "".join(pnr)
        self.area_code = pnr[0]
        self.exchange_code = pnr[1]
        self.subscriber_number = pnr[2]

    def pretty(self):
        return "(" + self.area_code + ") " + self.exchange_code + "-" + self.subscriber_number
        
