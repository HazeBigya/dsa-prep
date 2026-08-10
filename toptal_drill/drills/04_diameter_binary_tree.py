class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def diameter(root):
    best = [0]

    def dfs(node):
        if node is None:
            return -1
        left = dfs(node.left)
        right = dfs(node.right)
        best[0] = max(best[0], left + right + 2)
        return max(left, right) + 1

    dfs(root)
    return best[0]


#       1
#      /
#     2
#    / \
#   3   4
t1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)))
print(diameter(t1))  # expect 2

#        1
#       / \
#      2   3
#     / \
#    4   5
t2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
print(diameter(t2))  # expect 3

print(diameter(None))  # expect 0
print(diameter(TreeNode(1)))  # expect 0 (single node)
