# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:29:58 2024

@author: william.yates
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        inp_str = str(x)
        rev_str = inp_str[::-1]

        if inp_str == rev_str:
            return True
        else:
            return False