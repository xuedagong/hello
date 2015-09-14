# -*- coding:utf-8 -*-
'''
题目描述

输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

'''
前序遍历，首先获取的第一个节点是跟节点
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre)==0:
            return None

        if len(pre)==1:
            return TreeNode( pre[0] )

        root_node=TreeNode( pre[0] )
        index_i=tin.index(pre[0]) #根节点的位置

        left_pre=pre[1:index_i+1]
        right_pre=pre[index_i+1:]

        left_tin=tin[:index_i]
        right_tin=tin[index_i+1:]

        root_node.left=self.reConstructBinaryTree(left_pre,left_tin)
        root_node.right=self.reConstructBinaryTree(right_pre,right_tin)
        return root_node

if __name__ == '__main__':
    node1=Solution().reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
    pre=[1,2,4,7,3,5,6,8]
    tin=[4,7,2,1,5,3,8,6]
    index_i=tin.index(pre[0])
    left_pre=pre[1:index_i+1]
    right_pre=pre[index_i+1:]

    left_tin=tin[:index_i]
    right_tin=tin[index_i+1:]
    print left_pre,left_tin
    print right_pre,right_tin
    print index_i
    print node1.val
    print node1.right.val

