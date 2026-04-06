from collections import deque

# 1. The standard Node definition
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root: TreeNode, val):
        # --- YOUR CODE GOES HERE ---
        node = root
        while node:
            if node.val == val:
                return node
            elif node.val > val:
                node = node.left
            else: node = node.right
        
        return None
        # ---------------------------

# 2. HELPER: Converts a list [4, 2, 7, 1, 3] to a Binary Tree
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

# 3. HELPER: Simple way to print your result for verification
def print_tree(root):
    if not root:
        print("None")
        return
    res = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # Clean up trailing Nones for a prettier look
    while res and res[-1] is None: res.pop()
    print(res)

# 4. VSCODE EXECUTION BLOCK
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1: root = [4,2,7,1,3], val = 2
    test_list = [4, 2, 7, 1, 3]
    target = 2
    
    root_node = build_tree(test_list)
    result = solution.searchBST(root_node, target)

    print(f"Searching for {target}...")
    print("Result Subtree:", end=" ")
    print_tree(result)