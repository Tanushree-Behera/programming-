class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Tree) -> bool:

        def is_valid_bst_recursive(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return is_valid_bst_recursive(node.left, min_val, node.val) and \
                   is_valid_bst_recursive(node.right, node.val, max_val)
        return is_valid_bst_recursive(root, float('-inf'), float('inf'))

root = Tree(2)
root.left = Tree(1)
root.right = Tree(3)

solution = Solution()
print(solution.isValidBST(root))
