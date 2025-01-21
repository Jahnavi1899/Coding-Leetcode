# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        temp = head
        prevNode = None

        while temp:
            kthNode = self.findkthnode(temp, k)
            

            if kthNode:
                nextNode = kthNode.next
                kthNode.next = None

                self.reverseLL(temp)
                if temp == head:
                    head = kthNode
                else:
                    prevNode.next = kthNode

                prevNode = temp
                temp = nextNode
            else:
                prevNode.next = temp
                break

        return head

    def reverseLL(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def findkthnode(self, head, k):
        curr = head
        k -= 1
        while k and curr.next:
            curr = curr.next
            k -= 1

        if k:
            return None
        
        return curr
    
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2

obj = Solution()
print(obj.reverseKGroup(head, k))