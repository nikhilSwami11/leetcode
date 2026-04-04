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
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(root, targetSum, curr_path):
            if not root:
                return
            
            curr_path.append(root.val)

            if not root.right and not root.left and targetSum == root.val:
                ans.append(list(curr_path))
            
            dfs(root.left, targetSum - root.val, curr_path)
            dfs(root.right, targetSum - root.val, curr_path)

            curr_path.pop()
            

        dfs(root, targetSum, [])
        return ans

        

# --- TEST SETUP ---
if __name__ == "__main__":
    # Now you can just copy-paste the list from LeetCode
    null = None  # Friendly helper for 'null' in LeetCode examples
    root = [5,4,8,11,null,13,4,7,2,null,null,5,1]
    targetSum = 22
    
    root = build_tree(root)
    sol = Solution()
    print("Result:", sol.pathSum(root, targetSum))





