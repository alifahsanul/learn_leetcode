'''
Given the root of a binary tree, check whether it is a mirror of itself
(i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
'''


class Solution(object):
    def isSymmetric(self, root):
        """
        Recursive DFS mirror check.

        Idea:
        - A tree is symmetric if its left subtree is a mirror of its right subtree.
        - Two nodes are mirrors if:
          1) Their values are equal.
          2) Left child of one mirrors right child of the other.
          3) Right child of one mirrors left child of the other.
        """
        def mirror(left_node, right_node):
            if left_node is None and right_node is None:
                return True
            if left_node is None or right_node is None:
                return False
            if left_node.val != right_node.val:
                return False

            return (
                mirror(left_node.left, right_node.right)
                and mirror(left_node.right, right_node.left)
            )

        if root is None:
            return True
        return mirror(root.left, root.right)

    def isSymmetricIterative(self, root):
        """
        Iterative BFS mirror check using a queue of node pairs.
        """
        if root is None:
            return True

        queue = [(root.left, root.right)]

        while queue:
            left_node, right_node = queue.pop(0)

            if left_node is None and right_node is None:
                continue
            if left_node is None or right_node is None:
                return False
            if left_node.val != right_node.val:
                return False

            queue.append((left_node.left, right_node.right))
            queue.append((left_node.right, right_node.left))

        return True


# ---- Custom tests (run this file directly) ----
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    """
    Build a binary tree from level-order array representation.
    Example: [1, 2, 2, 3, 4, 4, 3]
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
        # (level_order_values, expected_is_symmetric)
        ([1, 2, 2, 3, 4, 4, 3], True),
        ([1, 2, 2, None, 3, None, 3], False),
        ([1], True),
        ([1, 2, 2, 3, None, None, 3], True),
        ([1, 2, 2, None, 3, 3, None], True),
    ]

    for values, expected in tests:
        root = build_tree(values)
        got_recursive = s.isSymmetric(root)
        got_iterative = s.isSymmetricIterative(root)
        print(
            "tree =",
            values,
            "| recursive =",
            got_recursive,
            "| iterative =",
            got_iterative,
            "| ok =",
            got_recursive == expected and got_iterative == expected,
        )
