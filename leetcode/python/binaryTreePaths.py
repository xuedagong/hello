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
#根据一行的输入来生成树  
#   1
#  /   \
# 2     3
#  \
#   5
#其输入为 1 2 3 # 5
def create_tree():
    
    lst=raw_input('请输入').split(" ")
    root=TreeNode(lst[0]);
    node_lst=[]
    node_lst.append(root)
    i=1
    while i <len(lst):
        this_node=node_lst[0]
        if lst[i]!='#':
            this_node.left=TreeNode( int(lst[i]) )
            node_lst.append(this_node.left)
        else:
            this_node.left=None
        
        if lst[i+1]!='#':
            this_node.right=TreeNode( int(lst[i+1]) )
            node_lst.append(this_node.right)
        else:
            this_node.right=None
        del node_lst[0]
        i=i+2
    return root
            
        
    

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

# node5=TreeNode(5)
# node2=TreeNode(2)
# node3=TreeNode(3)
# node1=TreeNode(1)
# node1.left=node2
# node1.right=node3
# node2.right=node5
node1=create_tree()

print Solution().binaryTreePaths(node1)