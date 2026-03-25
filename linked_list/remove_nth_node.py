'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

'''

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        Two-pointer trick with a fixed gap.

        - Use a `dummy` node so removing the head becomes a normal "skip next" operation.
        - Move `first` ahead by (n + 1) steps, so the gap between `first` and `second` is exactly (n + 1).
        - Then advance both pointers together until `first` hits None.
          At that moment, `second` is *right before* the node that is nth from the end,
          so we can remove it by `second.next = second.next.next`.
        """
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n+1):
            first = first.next
        while first is not None:
            first = first.next
            second = second.next
        # `second` now points to the node just before the target node.
        second.next = second.next.next
        return dummy.next


# ---- Custom tests (run this file directly) ----
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    head = None
    cur = None
    for v in values:
        n = ListNode(v)
        if head is None:
            head = n
            cur = n
        else:
            cur.next = n
            cur = n
    return head


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
        # (list_values, n, expected_after)
        ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
        ([1], 1, []),
        ([1, 2], 1, [1]),
        ([1, 2], 2, [2]),
        ([1, 2, 3], 3, [2, 3]),
        ([1, 2, 3, 4, 5], 3, [1, 2, 4, 5]),
    ]

    for values, n, expected in tests:
        head = build_list(values)
        got = to_list(s.removeNthFromEnd(head, n))
        print("before =", values, "| n =", n, "| after =", got, "| ok =", got == expected)
