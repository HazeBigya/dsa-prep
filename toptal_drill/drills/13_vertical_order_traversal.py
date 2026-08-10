from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def verticle_order(root):
    if not root:
        return []
    columns = defaultdict(list)
    queue = deque([(root, 0)])
    while queue:
        node, col = queue.popleft()
        columns[col].append(node.val)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    result = []
    for c in dict(sorted(columns.items())):
        result.append(columns[c])
    return result


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(verticle_order(root))
