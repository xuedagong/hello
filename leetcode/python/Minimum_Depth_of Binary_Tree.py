#coding=utf-8
'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #如何才能获取最小的深度呢？？  获取到每个叶子节点，比较这些叶子节点所在的深度。从而求出最小值
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        left_depth=0
        right_depth=0
        if root.left is not None:
            left_depth=1+self.minDepth(root.left)
        else:
            left_depth=2**32 #不作考虑
        if root.right is not None:
            right_depth=1+self.minDepth(root.right)
        else:
            right_depth=2**32 #不作考虑

        if left_depth<right_depth:
            return left_depth
        else:
            return right_depth
if __name__ == '__main__':
    root=TreeNode(1)
    root.left=TreeNode(2)
    print Solution().minDepth(root) # 结果为2


