# Reverse digits of an integer.
# 
# Example1: x = 123, return 321
# Example2: x = -123, return -321
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new_x=0
        old_x=x
        x=abs(x)
        while x/10:
            temp=x%10
            new_x=new_x*10+temp
            x=x/10
        new_x=new_x*10+x
        if old_x<0:
            new_x=-new_x
        if abs(new_x)>2**31 :
            return 0
        return new_x
print Solution().reverse(-1563847412)
print 2**31
        
        