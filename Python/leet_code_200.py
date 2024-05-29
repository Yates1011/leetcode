# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:32:11 2024

@author: william.yates
"""

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

rows, cols = len(grid), len(grid[0])
a = []

for i in range(rows):
    a.append(list(map(int, grid[i])))


def dfs(grid, i, j):
    # the base cases where traversal should stop
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
        return
    # mark the element as visited so that it won't be taken into account if visited again
    grid[i][j] = '0'

    dfs(grid, i-1, j)

    dfs(grid, i+1, j)

    dfs(grid, i, j-1)

    dfs(grid, i, j+1)
