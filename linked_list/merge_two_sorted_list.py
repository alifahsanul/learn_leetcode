"""
You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists into one sorted list. The list should be made by splicing together
the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        tail = dummy

        # Splice nodes from the two lists in sorted order.
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remaining nodes (already sorted).
        tail.next = list1 if list1 is not None else list2
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
        # (list1_values, list2_values, expected_merged)
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
    ]

    for values1, values2, expected in tests:
        head1 = build_list(values1)
        head2 = build_list(values2)
        got = to_list(s.mergeTwoLists(head1, head2))
        print(
            "list1 =",
            values1,
            "| list2 =",
            values2,
            "| merged =",
            got,
            "| ok =",
            got == expected,
        )