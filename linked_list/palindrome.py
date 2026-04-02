"""
Given the head of a singly linked list, return true if it is a palindrome
or false otherwise.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 10^5].
0 <= Node.val <= 9
"""


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool

        O(n) time, O(1) extra memory approach:

        - Use `slow`/`fast` pointers to find the middle:
          `slow` moves 1 step, `fast` moves 2 steps.
          When `fast` reaches the end, `slow` is at (or just past) the midpoint.

        - Reverse the second half of the list starting at `slow`.
          After reversing, `prev` becomes the head of the reversed second half.

        - Compare nodes from the start (`first`) and from the reversed half (`second`).
          We only need to walk `second` until it ends; if all values match, it's a palindrome.
        """
        if head is None or head.next is None:
            return True

        # Find the middle using the tortoise & hare trick.
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half starting from `slow`.
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # Compare the first half with the reversed second half.
        first = head
        second = prev
        result = True
        while second:
            if first.val != second.val:
                result = False
                break
            first = first.next
            second = second.next

        return result


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
        # (values, expected_is_palindrome)
        ([1, 2, 2, 1], True),
        ([1, 2], False),
        ([1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 4], False),
    ]

    for values, expected in tests:
        head = build_list(values)
        got = s.isPalindrome(head)
        print("values =", values, "| isPalindrome =", got, "| ok =", got == expected)