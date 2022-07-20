# https://leetcode.com/problems/flood-fill/
'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel
of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels
(also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.
Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
all pixels connected by a path of the same color as the starting pixel
(i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
Output: [[0,0,0],[0,0,0]]
Explanation: The starting pixel is already colored 0, so no changes are made to the image.
'''
# my des
def floodFill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    # fix color
    col = image[sr][sc]
    # fix size
    cols = len(image[0])
    rows = len(image)
    # not need to change
    if col == color:
        return image
    def fil(r, c):
        # change color
        if image[r][c] == col:
            image[r][c] = color
            # move
            if r >= 1:
                fil(r-1,c)
            if c >= 1:
                fil(r,c-1)
            if r+1 < rows:
                fil(r+1,c)
            if c+1 < cols:
                fil(r,c+1)
    fil(sr,sc)
    return image

# des opt
def floodFill2(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    rows = len(image)
    cols = len(image[0])
    color_to_change = image[sr][sc]
    def dfs(r, c):
        nonlocal rows, cols, newColor, image

        if r < 0 or c < 0 or r>rows-1 or c>cols-1 or image[r][c]==newColor or image[r][c]!=color_to_change:
            return

        image[r][c] = newColor
        # radiate in four directions
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)

    dfs(sr, sc)
    return image