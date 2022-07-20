# https://leetcode.com/problems/middle-of-the-linked-list/
'''
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
'''
# my des
def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    d = {}
    i = 1
    # if list with 1 element
    d[0] = head
    while head:
        d[i] = head.next
        head = head.next
        i += 1
    return d[(i-1) // 2]

# des opt
def middleNode1(head):
    # While slow moves one step forward, fast moves two steps forward.
    # Finally, when fast reaches the end, slow happens to be in the middle of the linked list.
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow