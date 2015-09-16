# -*- coding:utf-8 -*-
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个非递减序列的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
'''
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        n=len(rotateArray)
        if n==0:
            return 0
        for i in xrange(n-1):
            if rotateArray[i]>rotateArray[i+1]:
                return rotateArray[i+1]
        return rotateArray[0]

if __name__ == '__main__':
    print Solution().minNumberInRotateArray([])