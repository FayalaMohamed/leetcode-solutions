# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = 0
        x = 1
        it = l1
        while it : 
            n1 += it.val * x
            x *= 10
            it = it.next

        n2 = 0
        x = 1
        it = l2
        while it : 
            n2 += it.val * x
            x *= 10
            it = it.next
        
        n = n1 + n2
        
        prev = None
        for x in str(n):
            newNode = ListNode(val=int(x), next=prev)
            prev = newNode
        return prev
            