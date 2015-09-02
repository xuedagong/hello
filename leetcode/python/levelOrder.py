#coding=utf-8
'''
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.make_q([root], [])
        
    def make_q(self,root_lst,global_lst):
        one_list=[]
        new_root_lst=[]
        for item in root_lst:
            if item is not None:
                one_list.append(item.val)
                new_root_lst.append(item.left)
                new_root_lst.append(item.right)
        if len(one_list)>0:
            global_lst.append(one_list)
        if len(new_root_lst)>0:
            return self.make_q(new_root_lst,global_lst)
        else:
            return global_lst
        
            
            
        
        
        