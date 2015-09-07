#coding=utf-8
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix) #一共有多少行
        if m==0:
            return False
        n=len(matrix[0]) #一共有多少列
        max_i=0
        for item in matrix[0]:
            if item>target:
                break
            max_i+=1    #第一行 的第几个
        for k in xrange(max_i): #列的循环
            for j in xrange(m):#行的的循环
                if matrix[j][k]==target:
                    return True
                if matrix[j][k]>target:
                    break
        return False
if __name__ == '__main__':
    lst=[[1, 4,  7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30] ]
    # lst=[]
    print Solution().searchMatrix(lst,5)
    print Solution().searchMatrix(lst,20)
    print lst


