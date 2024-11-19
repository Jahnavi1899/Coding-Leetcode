# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head:ListNode, n):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        rev_head = prev
        prev, curr = None, rev_head
        n -= 1
        while n:
            prev = curr
            curr = curr.next
            n = n-1

        prev.next = curr.next
        curr.next = None

        prev, curr = None, rev_head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


head = [1,2,3,4,5]
n = 2

obj = Solution()
print(obj.removeNthFromEnd(head, n))