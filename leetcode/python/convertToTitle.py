#coding=utf-8
'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
'''
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        #我的意思是26进制
        strs=""

        while n>0:
            temp=n%26
            if temp==0:
                temp=26
            temp_to_str=chr( ord('A')+temp-1 )
            strs=temp_to_str+strs
            n=(n-1)/26
        return strs
if __name__ == '__main__':
    print Solution().convertToTitle(26)
