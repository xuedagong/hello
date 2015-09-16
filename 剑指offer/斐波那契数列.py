# -*- coding:utf-8 -*-
'''
题目描述

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
'''
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        now_n=2
        a=1
        b=1
        while now_n<n:
            temp=b
            b=a+b
            a=temp
            now_n+=1
        return b
if __name__ == '__main__':
    for i in xrange(10):
        print i,Solution().Fibonacci(i)
