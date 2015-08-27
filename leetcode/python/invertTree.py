#codint=utf-8
'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.Recu(root)
        return root
    def Recu(self,root):
        if root is None:#是空树
            return
        
        if root.left is None and root.right is None:#是叶子节点
            return
        temp=root.left
        root.left=root.right
        root.right=temp 
        if root.left is not  None:# 左节点 不为空
            self.invertTree(root.left)
        if root.right is not   None:# 右节点 不为空
            self.invertTree(root.right)

        