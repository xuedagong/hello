# -*- coding:utf-8 -*-
'''
题目描述

输入一个链表，从尾到头打印链表每个节点的值。
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode is None:
            return ""
        cur=listNode
        lst=[]
        while cur is not None:
            lst.append(cur.val)
            cur=cur.next
        lst.reverse()
        return lst

if __name__ == '__main__':
    node1=ListNode(67)
    node1.next=ListNode(0)
    node1.next.next=ListNode(24)
    node1.next.next.next=ListNode(58)
    print Solution().printListFromTailToHead(node1)
