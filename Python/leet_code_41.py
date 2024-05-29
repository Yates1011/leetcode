# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:43:17 2024

@author: william.yates
"""

from typing import List
        
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1
        
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

test_cases = [
    [],
    [-1, -2, -3],
    [1, 2, 0],
    [3, 4, -1, 1],
    [7, 8, 9, 11, 12],
    [1, 1, 2, 2, 3, 3],
]


sol = Solution()

for nums in test_cases:
    result = sol.firstMissingPositive(nums)
    print(f"For nums = {nums}, first missing positive is {result}")      
        
        
        




