# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
The binary tree has the following definition:
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.
Example 1:
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer
to point to its next right node, just like in Figure B. The serialized output is in level order as connected
by the next pointers, with '#' signifying the end of each level.
Example 2:
Input: root = []
Output: []
'''
# des opt
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        if root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root

# des2
class Solution(object):
    def connect(self, root):
        if not root: return root
        if root.left:
            left, right = root.left, root.right
            self.connect(left)
            self.connect(right)
            while left:
                left.next = right
                left, right = left.right, right.left
        return root