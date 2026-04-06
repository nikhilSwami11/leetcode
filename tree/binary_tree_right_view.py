

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
    def rightSideView(self, root: TreeNode):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        if not root:
            return []
        # root and level.
        q = deque([(root, 0)])
        level_visited = set()
        ans = []
        
        while q:
            node, level = q.popleft()
            if level not in level_visited:
                ans.append(node.val)
                level_visited.add(level)
            
            if node.right:
                q.append((node.right, level+1))
            if node.left:
                q.append((node.left, level+1))
        return ans
            






# --- LOCAL TESTING BLOCK ---

if __name__ == "__main__":
    # Now you can just copy-paste the list from LeetCode
    null = None  # Friendly helper for 'null' in LeetCode examples
    data = [1,2,3,4,null,null,null,5]
    
    root = build_tree(data)
    sol = Solution()
    print("Result:", sol.rightSideView(root))




# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        