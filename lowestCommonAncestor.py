class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root or root == p or root == q:
        return root
    left_lca = lowestCommonAncestor(root.left, p, q)
    right_lca = lowestCommonAncestor(root.right, p, q)

    if left_lca and right_lca:
        return root
    return left_lca if left_lca else right_lca


node_3 = TreeNode(3)
node_5 = TreeNode(5)
node_1 = TreeNode(1)
node_6 = TreeNode(6)
node_2 = TreeNode(2)
node_0 = TreeNode(0)
node_8 = TreeNode(8)
node_7 = TreeNode(7)
node_4 = TreeNode(4)


node_3.left = node_5
node_3.right = node_1
node_5.left = node_6
node_5.right = node_2
node_1.left = node_0
node_1.right = node_8
node_2.left = node_7
node_2.right = node_4


lca_node = lowestCommonAncestor(node_3, node_5, node_1)
print(f"The LCA of 5 and 1 is: {lca_node.val}") 
