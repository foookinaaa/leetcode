# https://leetcode.com/problems/max-area-of-island/
'''
You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
The area of an island is the number of cells with a value 1 in the island.
Return the maximum area of an island in grid. If there is no island, return 0.
Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0
'''
# des opt
def maxAreaOfIsland(grid):
    seen = set()
    def area(r, c):
        # if we see it before or it's not exist
        if not (0 <= r < len(grid) and 0 <= c < len(grid[0])
                and (r, c) not in seen and grid[r][c]):
            return 0
        seen.add((r, c))
        #print(r,c)
        # 1 + right + left + up + down
        return (1 + area(r+1, c) + area(r-1, c) +
                area(r, c-1) + area(r, c+1))

    return max(area(r, c)
               for r in range(len(grid))
               for c in range(len(grid[0])))

# des opt
class Solution():
    def maxAreaOfIsland1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # t: O(rc) s: O(1)
        max_area = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    max_area = max(max_area, self.explore(grid, r, c))
        return max_area

    def explore(self, grid, r, c):
        if (r < 0 or r >= len(grid)) or (c < 0 or c >= len(grid[r])):
            return 0
        if grid[r][c] == 0:
            return 0
        # mark as visited
        grid[r][c] = 0
        return 1 + self.explore(grid, r - 1, c) + self.explore(grid, r, c - 1) \
               + self.explore(grid, r + 1, c) + self.explore(grid, r, c + 1)