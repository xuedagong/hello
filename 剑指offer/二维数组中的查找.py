# -*- coding:utf-8 -*-
'''
题目描述

在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, array, target):
        k=len(array)#有多少行
        j=len(array[0])#有多少列
        find_x,find_y=0,0
        while find_x<j and array[find_x][0]<=target:
            find_y=0
            while find_y<k and array[find_y][find_x]<target:
                find_y+=1
            if find_y<j and array[find_y][find_x]==target:
                return True
            #这里 就是大于了
            find_x+=1
        return False
if __name__ == '__main__':
    print Solution().Find([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]],7)

        # write code here
