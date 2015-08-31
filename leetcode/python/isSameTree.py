#coding=utf-8
'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is  None or  q is None:
            if p is None and q is None:
                return  True
            else:
                return False


        if p.val!=q.val:
            return False

        if p.val==q.val and p.left is None and p.right is None and q.left is None and q.right is None:
            return True



        a=False
        b=False

        a=self.isSameTree(p.left,q.left)

        b=self.isSameTree(p.right,q.right)




        if a and b:
            return  True
        return False

        