from collections import deque

class TreeNode(object):
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
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        count = 3
        stack = [(root, root.value)]

        

# --- TEST SETUP ---
if __name__ == "__main__":
    # Now you can just copy-paste the list from LeetCode
    null = None  # Friendly helper for 'null' in LeetCode examples
    root = [10,5,-3,3,2,null,11,3,-2,null,1], 
    targetSum = 8
    
    root = build_tree(root)
    sol = Solution()
    print("Result:", sol.pathSum(root, targetSum))