from listNode import ListNode
from solution import Solution
Run=Solution()
l1=ListNode(val=2,next=ListNode(val=4,next=ListNode(val=3)))
l2=ListNode(val=5,next=ListNode(val=6,next=ListNode(val=4)))

Run.addTwoNumbers(l1,l2)