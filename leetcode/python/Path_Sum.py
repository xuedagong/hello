#coding=utf-8
'''
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        path,result=[],[]
        self.binaryTreePathSumRecu(root,path,result)
        # print result
        for item in result:
            if sum==item:
                return True

        return False
        #到叶子节点的和是否等于 sum
    def binaryTreePathSumRecu(self,node,path,result):
        if node is None:##node是空节点
            return
        if node.left is node.right is None:##node是个叶子节点
            lef_sum=0 #计算访问到这个节点值的和
            lst=[]
            for n in path:
                lef_sum=lef_sum+n.val
                lst.append(n.val)
            lef_sum+=node.val
            result.append( lef_sum );
        if node.left:
            path.append(node)
            self.binaryTreePathSumRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathSumRecu(node.right, path, result)
            path.pop()


if __name__ == '__main__':
    root=TreeNode(2)
    node2=TreeNode(2)
    node1=TreeNode(1)
    root.left=node2
    root.right=node1
    node2.right=TreeNode(3)
    node1.left=TreeNode(1)
    print Solution().hasPathSum(root,7)


