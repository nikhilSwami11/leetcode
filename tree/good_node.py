# --- LEETCODE BOILERPLATE ---

from collections import deque


class TreeNode(object):
    """Definition for a binary tree node."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    """
    Converts a list into a binary tree structure.
    Input: [3, 1, 4, 3, None, 1, 5]
    """
    if not nodes:
        return None
    
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(nodes):
        curr = queue.popleft()
        
        # Process left child
        if i < len(nodes) and nodes[i] is not None:
            curr.left = TreeNode(nodes[i])
            queue.append(curr.left)
        i += 1
        
        # Process right child
        if i < len(nodes) and nodes[i] is not None:
            curr.right = TreeNode(nodes[i])
            queue.append(curr.right)
        i += 1
        
    return root

class Solution(object):
    def goodNodes(self, root : TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """
        # TODO: Implement your logic her
        return self.countGoodNodes(root, root.val)
        
    def countGoodNodes(self, root : TreeNode, max_val: int):
        if root == null:
            return 0
        
        maxi = max(max_val, root.val)
        return  (1 if maxi==root.val else 0 ) +self.countGoodNodes(root.left,maxi) + self.countGoodNodes(root.right, maxi)



# --- LOCAL TESTING BLOCK ---

if __name__ == "__main__":
    # Now you can just copy-paste the list from LeetCode
    null = None  # Friendly helper for 'null' in LeetCode examples
    data = [1]
    
    root = build_tree(data)
    sol = Solution()
    print("Result:", sol.goodNodes(root))