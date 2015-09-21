# -*- coding:utf-8 -*-
'''
题目描述

将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
'''
# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        s_lst=list(s)
        if len(s_lst)==0:
            return 0
        item=s[0]
        sum=0
        if item=='-':
            for i in xrange(1,len(s_lst)):
                if self.is_dig(s_lst[i]):
                    sum=sum*10+ord(s_lst[i])-ord('0')
                else:
                    return 0
            sum=sum*(-1)
        elif item=='+':
            for i in xrange(1,len(s_lst)):
                if self.is_dig(s_lst[i]):
                    sum=sum*10+ord(s_lst[i])-ord('0')
                else:
                    return 0
            sum=sum

        else:
            for i in xrange(0,len(s_lst)):
                if self.is_dig(s_lst[i]):
                    sum=sum*10+ord(s_lst[i])-ord('0')
                else:
                    return 0
        return sum
    def is_dig(self,item):
        if ord(item)>=ord('0') and ord(item)<=ord('9'):
            return True
        else:
            return False
        # write code here

if __name__ == '__main__':
    print Solution().StrToInt('-12')
    print Solution().StrToInt("1a33")
