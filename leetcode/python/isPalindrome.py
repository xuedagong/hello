'''
Determine whether an integer is a palindrome. Do this without extra space.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_x=str(x)

        lens=len(str_x)
        for i in range(lens/2):
            if str_x[i]!=str_x[lens-1-i]:
                return False
        return True
print Solution().isPalindrome(12)
        