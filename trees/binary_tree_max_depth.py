'''
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
'''


class Solution(object):
    def maxDepth(self, root):
        """
        Depth-First Search (DFS), recursively.

        Idea:
        - If the current node is None, its depth is 0.
        - Otherwise, the depth of this node is:
            1 + max(depth_of_left_subtree, depth_of_right_subtree)

        Why this works:
        - The tree depth is defined as the number of nodes in the longest path
          from root to a leaf.
        - For any node, the longest path going down from it must be either in
          its left subtree or right subtree.
        - So we solve both sides and keep the larger one.
        """
        if root is None:
            return 0

        # Recursively compute depth on both branches.
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # Count the current node (+1), then attach the deeper side.
        return 1 + max(left_depth, right_depth)


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
        # (level_order_values, expected_max_depth)
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([1], 1),
        ([1, 2, 3, 4, None, None, 5], 3),
    ]

    for values, expected in tests:
        root = build_tree(values)
        got = s.maxDepth(root)
        print("tree =", values, "| depth =", got, "| ok =", got == expected)