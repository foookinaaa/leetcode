# https://leetcode.com/problems/move-zeroes/
'''
Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]
'''
# my des
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)-2
    r = len(nums)-1
    while l >= 0:
        if nums[l] == 0:
            # move on one step all elements
            for i in range(l,r):
                nums[i] = nums[i+1]
            # add zero at the end
            nums[r] = 0
            r -= 1
        l -= 1

# des opt
def moveZeroes2(nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
        print(zero,nums)

nums = [0,1,0,3,12]
moveZeroes2(nums)