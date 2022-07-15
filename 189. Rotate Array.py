# https://leetcode.com/problems/rotate-array/
'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''
# my des
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    # boundary case
    if len(nums) <= 1:
        return nums
    # rotate k steps + residual
    while k > len(nums):
        k = k % len(nums)
    # last part
    temp = nums[-k:]
    last = k
    start = 0
    while last < len(nums) and last != 0:
        # part of nums to temp
        nums[start:last], temp = temp, nums[start:last]
        # move pointers on k steps
        start = last
        last += k
    # last step
    if last >= len(nums):
        nums[start:len(nums)] = temp[:(len(nums)-start)]
    print(nums)

# des opt
def rotate1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    a = [0] * len(nums)
    for i in range(len(nums)):
        a[(i+k)%len(nums)] = nums[i] #recycle
        print(a)
    for i in range(len(nums)):
        nums[i] = a[i]
    print(nums)

# des opt
def rotate2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    k = k % len(nums)
    count = 0
    start = 0
    while count < len(nums):
        current = start
        prev = nums[start] #store the value in the position

        while True:
            print(start, current, nums)
            next = (current + k) % len(nums) #
            print('next', next)
            temp = nums[next] #store it temporaly
            print('temp', temp)
            nums[next] = prev #overide the next
            print('nn', prev)
            prev = temp #reset prev
            print('prev', prev)
            current = next #reset current
            print('cur', current)
            count += 1
            print('cnt', count)

            if start == current:
                print('---')
                break

        start += 1

# des opt
def reverse(nums, start, end):
    while start < end: #
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1
def rotate3(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    # nums = [1 2 3 4 5 6 7]
    k %= len(nums)
    # reverse all list [7 6 5 4 3 2 1]
    reverse(nums,0,len(nums)-1)
    # reversing first k numbers : [5 6 7 4 3 2 1]
    reverse(nums,0, k-1)
    # revering last n-k numbers : [5 6 7 1 2 3 4]
    reverse(nums,k, len(nums)-1)
    print(nums)

nums = [1, 2,3,4,5,6]
k = 2
print(rotate3(nums, k))
