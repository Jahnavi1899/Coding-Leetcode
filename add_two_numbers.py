class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        ll_sum = ListNode()
        current = ll_sum
        current.val = 0
        current.next = None
        while l1.next != None or l2.next != None:
            current.val = current.val + (l1.val + l2.val) % 10
            current.next = ListNode()
            current.next.val = (l1.val + l2.val) // 10
            current = current.next
            l1 = l1.next
            l2 = l2.next
            print(ll_sum)
        return ll_sum

[2,4,3]
[5,6,4]
n3 = ListNode(val = 3)
n2 = ListNode(val = 4, next = n3)
l1 = ListNode(val = 2, next = n2)

m3 = ListNode(val = 4)
m2 = ListNode(val = 6, next = m3)
l2 = ListNode(val = 5, next = m2)

# while l1 != None:
#     print(l1.val)
#     l1 = l1.next
# while l2 != None:
#     print(l2.val)
#     l2 = l2.next
print(l1)
add_nums = Solution().addTwoNumbers(l1, l2)
while add_nums != None:
    print(add_nums.val)
    add_nums = add_nums.next