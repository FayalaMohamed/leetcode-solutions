# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return
        
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        it = slow.next
        prev = None
        slow.next = None
        while it:
            temp = it.next
            it.next = prev
            prev = it
            it = temp
        
        it = head
        it2 = prev
        while it2 :
            temp1 = it.next
            temp2 = it2.next
            it.next = it2
            it2.next = temp1
            it = temp1
            it2 = temp2


