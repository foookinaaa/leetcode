# https://leetcode.com/problems/binary-search/
'''
Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
# my des
def search(nums, target):
    l = 0
    r = len(nums)-1
    while l < r:
        m = (l+r) // 2 + 1
        if target > nums[m]:
            l = m
        elif target == nums[m]:
            return m
        else:
            r = m-1
        print(l,r)
    if target == nums[r]:
        return r
    return -1

# des opt1
def search1(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
        print(left, right, pivot)
    return -1

nums = [-1,0,3,5,9,12]
target = 2
print(search1(nums,target))

