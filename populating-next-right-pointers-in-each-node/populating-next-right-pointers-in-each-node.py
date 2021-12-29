"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.left: return root
        self.connect(root.left)
        self.connect(root.right)
        left = root.left
        right = root.right
        left.next= right
        
        while left.right:
            left = left.right
            right = right.left
            left.next = right
            
        return root