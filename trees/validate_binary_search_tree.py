'''
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys strictly less than the node's key.
- The right subtree of a node contains only nodes with keys strictly greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]
Output: true

Example 2:
Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.

Constraints:
The number of nodes in the tree is in the range [1, 104].
-2^31 <= Node.val <= 2^31 - 1
'''


class Solution(object):
    def isValidBST(self, root):
        """
        DFS with valid value range per subtree.

        Idea:
        - Each node must lie in an open interval (low, high): low < val < high.
        - Root is in (-inf, +inf).
        - Left child of a node with value v must satisfy low < x < v.
        - Right child must satisfy v < x < high.

        Why this works:
        - BST property is local (parent vs child) but also global (e.g. a node in
          the right subtree must be greater than every ancestor on the path).
        - Passing (low, high) down encodes all ancestor constraints.
        """
        def valid(node, low, high):
            if node is None:
                return True
            if not (low < node.val < high):
                return False
            return (
                valid(node.left, low, node.val)
                and valid(node.right, node.val, high)
            )

        return valid(root, float('-inf'), float('inf'))


# ---- Custom tests (run this file directly) ----
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """
    Build a binary tree from level-order array representation.
    Example: [3, 9, 20, None, None, 15, 7]
    """
    if not values:
        return None

    nodes = [TreeNode(v) if v is not None else None for v in values]
    child_index = 1

    for i in range(len(nodes)):
        if nodes[i] is None:
            continue
        if child_index < len(nodes):
            nodes[i].left = nodes[child_index]
            child_index += 1
        if child_index < len(nodes):
            nodes[i].right = nodes[child_index]
            child_index += 1

    return nodes[0]


if __name__ == "__main__":
    s = Solution()

    tests = [
        # (level_order_values, expected_is_valid_bst)
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1], True),
        ([2, 2, 2], False),
        ([5, 4, 6, None, None, 3, 7], False),
    ]

    for values, expected in tests:
        root = build_tree(values)
        got = s.isValidBST(root)
        print("tree =", values, "| valid =", got, "| ok =", got == expected)
