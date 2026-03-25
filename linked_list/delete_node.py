'''
There is a singly-linked list head and we want to delete a node node in it.

You are given the node to be deleted node. You will not be given access to the first node of head.

All the values of the linked list are unique, and it is guaranteed that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.
Custom testing:

For the input, you should provide the entire linked list head and the node to be given node. node should not be the last node of the list and should be an actual node in the list.
We will build the linked list and pass the node to your function.
The output will be the entire list after calling your function.

'''

class Solution(object):
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


# ---- Custom tests (run this file directly) ----
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    head = None
    cur = None
    nodes_by_val = {}
    for v in values:
        n = ListNode(v)
        nodes_by_val[v] = n
        if head is None:
            head = n
            cur = n
        else:
            cur.next = n
            cur = n
    return head, nodes_by_val


def to_list(head):
    out = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out


if __name__ == "__main__":
    s = Solution()

    tests = [
        # (list_values, value_to_delete, expected_after)
        ([4, 5, 1, 9], 5, [4, 1, 9]),
        ([4, 5, 1, 9], 1, [4, 5, 9]),
        ([1, 2], 1, [2]),
    ]

    for values, delete_val, expected in tests:
        head, nodes = build_list(values)
        s.deleteNode(nodes[delete_val])
        got = to_list(head)
        print("before =", values, "| delete =", delete_val, "| after =", got, "| ok =", got == expected)
