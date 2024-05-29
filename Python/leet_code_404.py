# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:12:13 2024

@author: william.yates
"""

# root = [3,9,20,None,None,15,7]

class TreeNode:
    def __init__(self, value):
        self.val = value  
        self.left = None  
        self.right = None  


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root is None:
            return 0
      
        sum_left_leaves = 0
      
        if root.left and root.left.left is None and root.left.right is None:
            sum_left_leaves += root.left.val  
      
        sum_left_leaves += self.sumOfLeftLeaves(root.left)
      
        sum_left_leaves += self.sumOfLeftLeaves(root.right)

        return sum_left_leaves

def build_tree():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root

def test_solution():
    solution = Solution()
    root = build_tree()
    result = solution.sumOfLeftLeaves(root)
    print("Sum of left leaves:", result)  # Expected output: 9 + 15 = 24

test_solution()

        
        



