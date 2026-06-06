from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Dummy baseline implementation: just return a single node root
        # Replace this with your recursive Divide and Conquer code!
        index_map = {val:i for i,val in enumerate(inorder)}

        def helper(left_in, right_in):
            if left_in > right_in:
                return None

            val = postorder.pop()
            root = TreeNode(val)

            root.right = helper(index_map[val]+1,right_in)
            root.left = helper(left_in, index_map[val]-1)
            
            return root
        return helper(0,len(inorder)-1)

# ==========================================
# Helper functions to test your code locally
# ==========================================

def print_tree_visual(root: Optional[TreeNode], level: int = 0, prefix: str = "Root: "):
    """Helper to print the tree structure visually in the console (rotated 90 deg)."""
    if root is None:
        return
    print_tree_visual(root.right, level + 1, "R---> ")
    print("    " * level + prefix + str(root.val))
    print_tree_visual(root.left, level + 1, "L---> ")

# Test Case Execution
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    # Inorder:   [9, 3, 15, 20, 7]  (Left, Root, Right)
    # Postorder: [9, 15, 7, 20, 3]  (Left, Right, Root)
    inorder_input = [9, 3, 15, 20, 7]
    postorder_input = [9, 15, 7, 20, 3]
    
    print("Constructing tree...")
    tree_root = solution.buildTree(inorder_input, postorder_input)
    
    print("\nVisualized Tree Structure:")
    print_tree_visual(tree_root)