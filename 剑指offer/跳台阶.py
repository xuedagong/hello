# -*- coding:utf-8 -*-
'''
题目描述

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, n):
        # write code here
        if n==1:
            return 1
        if n==2:
            return 2
        now_n=2
        step_a=1
        step_b=2
        while now_n<n:
            temp=step_b
            step_b=step_a+step_b
            step_a=temp
            now_n+=1
        return step_b
if __name__ == '__main__':
    for i in xrange(1,10):
        print i,Solution().jumpFloor(i)

