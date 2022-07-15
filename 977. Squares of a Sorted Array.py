# https://leetcode.com/problems/squares-of-a-sorted-array/
'''
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
# my des
def sortedSquares(nums):
    # for find first not negative num
    i = 0
    # squares for negatives
    neg = []
    # for pointer to insert pos values in neg list
    k = 0
    # for all negatives combine squares in list neg
    while nums[i] < 0:
        neg.insert(0, nums[i] ** 2)
        i += 1
        # if all numbers are negative
        if i == len(nums):
            break
    # for not neg nums
    for j in range(i, len(nums)):
        cur = nums[j] ** 2
        #print(cur, neg, k)
        # if there are neg elements in nums
        if len(neg) > 0:
            # find the place to insert pos
            while cur > neg[k]:
                k += 1
                if k >= len(neg):
                    break
            neg.insert(k, cur)
        # if only not neg values in nums
        else:
            neg.append(cur)
    return neg

# des opt
def sortedSquares1(A):
    return_array = [0] * len(A)
    write_pointer = len(A) - 1
    left_read_pointer = 0
    right_read_pointer = len(A) - 1
    left_square = A[left_read_pointer] ** 2
    right_square = A[right_read_pointer] ** 2
    while write_pointer >= 0:
        print(left_read_pointer, right_read_pointer, write_pointer)
        if left_square > right_square:
            return_array[write_pointer] = left_square
            left_read_pointer += 1
            left_square = A[left_read_pointer] ** 2
        else:
            return_array[write_pointer] = right_square
            right_read_pointer -= 1
            right_square = A[right_read_pointer] ** 2
        write_pointer -= 1
    return return_array

nums = [-4,-1,0,3,10]
print(sortedSquares1(nums))