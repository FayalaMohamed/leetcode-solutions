# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        it = head
        prev = None
        while it:
            temp = it.next
            it.next = prev
            prev = it
            it = temp
        return prev