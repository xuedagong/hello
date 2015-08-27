#coding=utf-8
'''
Reverse a singly linked list.

click to show more hints.

Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_it(self):
        lst=[]
        temp=self
        while temp is not None:
            lst.append(temp.val)
            temp=temp.next
        print lst

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        #超过了2个节点
        last_node=None
        while head is not None and head.next is not None:
            temp=head.next
            head.next=last_node
            last_node=head
            head=temp

        head.next=last_node
        return head
mynode=ListNode(1)
mynode2=ListNode(2)
mynode.next=mynode2
mynode=Solution().reverseList(mynode)
mynode.print_it()

        