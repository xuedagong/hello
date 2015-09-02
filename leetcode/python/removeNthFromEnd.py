#coding=utf-8
'''
   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def print_it(self):
        cur=self
        lst=[]
        while cur is not None:
            lst.append(cur.val)
            cur=cur.next
        # print 999
        print lst

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        head_re=self.reverse(head)

        cur=head_re
        # exit(1)
        if n==1:#删除头
            return self.reverse(cur.next)
        i=0
        while i<n-2:
            i+=1
            cur=cur.next
        if cur.next is not None:
            cur.next=cur.next.next
        else:
            cur=None
        # head_re.print_it()
        return self.reverse(head_re)


        return head
    def reverse(self,head):
        pre,cur=None,head
        if head is None:
            return head
        while cur is not None:
            temp_next=cur.next
            cur.next=pre
            pre,cur=cur,temp_next
        return pre
node1=ListNode(3)
node1.next=ListNode(2)
node1.next.next=ListNode(4)

Solution().removeNthFromEnd(node1,2).print_it()

        