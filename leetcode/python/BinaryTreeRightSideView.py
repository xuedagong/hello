'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:
Given the following binary tree,
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
You should return [1, 3, 4].

'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        val_list=[]
        self.get_my([root],val_list)
        return val_list
    def get_my(self,node_lst,val_list):
        new_node_lst=[]
        if len(node_lst)==0:
            return

        for one_node in node_lst:
            temp=one_node.val
            if one_node.left is not None:
                new_node_lst.append(one_node.left)
            if one_node.right is not None:
                new_node_lst.append(one_node.right)
        val_list.append(temp)
        return self.get_my(new_node_lst,val_list)
if __name__ == '__main__':
    root=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    root.left=node2
    root.right=node3
    node2.right=TreeNode(5)
    node3.right=TreeNode(4)
    print Solution().rightSideView(root)



