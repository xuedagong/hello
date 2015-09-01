#coding=utf-8
'''
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        inta=int(a,2)
        intb=int(b,2)
        c=inta+intb
        return self.int2str(c)
    #将一个10进制数字转为 2进制表示的字符串
    def int2str(self,num):
        strs=""
        while num>0:
            temp=num%2
            
            strs=str(temp)+strs
            num=num/2
        if strs=="":
            return "0"
        return strs
print Solution().addBinary("0", "0")