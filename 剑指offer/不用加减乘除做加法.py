# -*- coding:utf-8 -*-
'''
题目描述

写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''

class Solution:
    def Add(self, num1, num2):
        # write code here
        if num2==0:
            return num1
        temp=int( num1^num2 )
        carry= int( (num1&num2)<<1  )
        return self.Add(temp,carry)


if __name__ == '__main__':
    print Solution().Add(111,899)
    print Solution().Add(-1,2)