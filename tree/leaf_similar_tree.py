# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

def build_tree(nodes: list) -> Optional[TreeNode]:
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):

        curr = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
            
    return root


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.get_leaves(root1) == self.get_leaves(root2)

    def get_leaves(self, node:Optional[TreeNode]):
        leaves = []

        if not node:
            return leaves
        
        stack = [node]

        while stack:
            root = stack.pop()

            if not root.left and not root.right:
                leaves.append(root.val)
            
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            
        return leaves
        


# Test Case 1
tree1 = build_tree([1,2,3])
tree2 = build_tree([1,3,2])

sol = Solution()
print(sol.leafSimilar(tree1, tree2))