'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
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
        print lst

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst=[]
        pre=ListNode(-1)
        pre.next=head
        cur=head
        while cur is not None:
            print cur
            if cur.val  not in lst:
                lst.append(cur.val)
                cur=cur.next
                pre=pre.next
            else:#del
#                 print 1
                pre.next=cur.next
                cur=cur.next
        return head
            
node1=ListNode(1)
node1.next=ListNode(1)     
# node1.next.next=ListNode(2)     
node1.print_it()
print Solution().deleteDuplicates(node1).print_it()    
        