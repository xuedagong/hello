# -*- coding:utf-8 -*-
'''
题目描述

一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number==1:
            return 1# 有一个抬价，只可能有一个跳法
        sum=1
        for i in xrange(1,number):#i表示最后一次跳的台阶数
            #n-i个
            sum+=self.jumpFloorII(number-i)
        return sum
if __name__ == '__main__':
    print Solution().jumpFloorII(3)