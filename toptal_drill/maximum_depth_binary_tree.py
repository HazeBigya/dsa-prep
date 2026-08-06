class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    if root is None:
        return 0
    left = max_depth(root.left)
    right = max_depth(root.right)
    return max(left, right) + 1


def show(node, depth=0):
    if node is None:
        return 0
    print("     " * depth + str(node.val))
    show(node.left, depth + 1)
    show(node.right, depth + 1)


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root2 = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3))
print(max_depth(root2))
show(root2)
