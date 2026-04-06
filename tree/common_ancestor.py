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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root, p,q).val


    def dfs(self,root, p, q):
        if not root:
            return
        
        if root.val == p or root.val == q:
            return root
        
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p,q)
        
        if left and right:
            return root

        return left or right






# --- LOCAL TESTING BLOCK ---

if __name__ == "__main__":
    # Now you can just copy-paste the list from LeetCode
    null = None  # Friendly helper for 'null' in LeetCode examples
    data = [3,5,1,6,2,0,8,null,null,7,4]
    p = 5
    q = 1
    
    root = build_tree(data)
    sol = Solution()
    print("Result:", sol.lowestCommonAncestor(root, p,q))