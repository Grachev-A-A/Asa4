class treeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right


def maxSum(firstNode):
    s = firstNode.value
    s1 = s2 = 0
    if firstNode.left is not None:
        s1 = maxSum(firstNode.left)
    if firstNode.right is not None:
        s2 = maxSum(firstNode.right)
    s += s1 if s1 > s2 else s2
    return s


node = treeNode(5,
                treeNode(4, treeNode(11, treeNode(7), treeNode(2))),
                treeNode(8, treeNode(13), treeNode(4, treeNode(5), treeNode(1)))
                )
print(maxSum(node))
