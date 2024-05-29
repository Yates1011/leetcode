# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:31:23 2024

@author: william.yates
"""

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

# grid = [[1]]

# grid = [[1,0]]

# grid = [[1,1],[1,1]]

perimeter = 0
rows, cols = len(grid), len(grid[0])

perimeter = 0

for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 1:
            perimeter += 4
            if c > 0 and grid[r][c-1] == 1:
                perimeter -= 2
            if r > 0 and grid[r-1][c] == 1:
                perimeter -= 2
                
                
