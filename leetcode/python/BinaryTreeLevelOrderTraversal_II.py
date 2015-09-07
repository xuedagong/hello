'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        my_lst=self.make_q([root], [])
        my_lst.reverse()
        return my_lst

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
if __name__ == '__main__':
    print 1