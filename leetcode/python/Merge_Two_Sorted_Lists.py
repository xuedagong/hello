'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return  l2
        if l2 is None:
            return l1


        if l1.val>l2.val:
             lst=ListNode(l2.val)
             l2=l2.next
        else:
             lst=ListNode(l1.val)
             l1=l1.next
        head=lst
        while l1 is not None and l2 is not None:
            if l1.val<l2.val:
                lst.next=l1
                lst=lst.next
                l1=l1.next
            else:
                lst.next=l2
                lst=lst.next
                l2=l2.next

        while l1 is not None:
            lst.next=l1
            lst=lst.next
            l1=l1.next

        while l2 is not None:
            lst.next=l2
            lst=lst.next
            l2=l2.next

        return head

        