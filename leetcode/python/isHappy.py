#coding=utf-8
'''
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer,
 replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
'''
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lst=[]
        while n!=1 and n not in lst:
            lst.append(n)
            n=self.find_next_num(n)
        if n==1:
            return True
        else:
            return False
    #拆分到下一个数字
    def find_next_num(self,n):
        sums=0
        while n>0:
            temp=n%10
            sums=sums+temp*temp
            n=n/10
        return sums
print Solution().isHappy(11)

