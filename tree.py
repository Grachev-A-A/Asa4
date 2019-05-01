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
                treeNode(4,
                         treeNode(11,
                                  treeNode(7),
                                  treeNode(2)
                                  )
                         ),
                treeNode(8,
                         treeNode(13),
                         treeNode(4,
                                  treeNode(5),
                                  treeNode(1)
                                  )
                         )
                )

Node = treeNode(5,
                treeNode(4, None,
                         treeNode(7,
                                  treeNode(11,
                                           treeNode(42),
                                           treeNode(14, None,
                                                    treeNode(66))
                                           ),
                                  treeNode(2))
                         ),
                treeNode(12,
                         treeNode(32),
                         treeNode(87,
                                  treeNode(43),
                                  treeNode(13))
                         )
                )

oneMoreNode = treeNode(1)  # Критический случай - нет ни одного поддерева
print(maxSum(Node))
print(maxSum(oneMoreNode))
print(maxSum(node))
