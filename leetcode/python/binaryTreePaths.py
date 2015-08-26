#coding=utf-8

# Time:  O(n * h)
# Space: O(h)
#
# Given a binary tree, return all root-to-leaf paths.
#
# For example, given the following binary tree:
#
#   1
#  /   \
# 2     3
#  \
#   5
# All root-to-leaf paths are:
#
# ["1->2->5", "1->3"]
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        result, path = [], []
        self.binaryTreePathsRecu(root, path, result)
        return result

    def binaryTreePathsRecu(self,node,path,result):
        if node is None:##node是空节点
            return
        if node.left is node.right is None:##node是个叶子节点
            ans=""
            for n in path:
                ans+=str(n.val)+"->"
            result.append( ans+str(node.val) );
        if node.left:
            path.append(node)
            self.binaryTreePathsRecu(node.left, path, result)
            path.pop()

        if node.right:
            path.append(node)
            self.binaryTreePathsRecu(node.right, path, result)
            path.pop()

node5=TreeNode(5)
node2=TreeNode(2)
node3=TreeNode(3)
node1=TreeNode(1)
node1.left=node2
node1.right=node3
node2.right=node5
print Solution().binaryTreePaths(node1)