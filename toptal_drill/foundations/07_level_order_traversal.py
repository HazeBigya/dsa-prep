from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root):
    if not root:
        return []
    result = []
    queue = deque([root])

    while queue:
        row_size = len(queue)
        row = []

        for _ in range(row_size):
            node = queue.popleft()
            row.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(row)

    return result


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(levelOrder(root))
