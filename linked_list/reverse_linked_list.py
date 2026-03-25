'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current is not None:
            # Save next node, then flip the current node's pointer.
            next = current.next
            current.next = prev
            # Move the sliding window forward.
            prev = current
            current = next
        return prev


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
        # (list_values, expected_after_reverse)
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
    ]

    for values, expected in tests:
        head = build_list(values)
        got = to_list(s.reverseList(head))
        print("before =", values, "| after =", got, "| ok =", got == expected)