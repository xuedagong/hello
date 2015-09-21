# -*- coding:utf-8 -*-
'''
题目描述

在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
'''
# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~返回任意重复的一个，赋值duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        a=numbers[0]
        for i in xrange(1,len(numbers)):
            a=a^numbers[i]
            if a==0:
                duplication.append(numbers[i])
                print numbers[i]
                return True
        return False

if __name__ == '__main__':
    lst=[]
    print 1&4&4
    exit(0)
    print Solution().duplicate([2,3,2],lst)
    print lst[0]