'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst=[]
        for item in s:
            if item in ["(","{","["]:
                lst.append(item)
            else:
                if len(lst)==0 or not self.isEqul(lst.pop(), item):
                    return False
    
        if len(lst)>0:
            return False
        return True
    def isEqul(self,s1,s2):
        if s1=='(' and s2==')':
            return True
        if s1=='{' and s2=='}':
            return True
        if s1=='[' and s2==']':
            return True
        return False
print Solution().isValid("([)]")
lst=[2,3,4]
print lst.pop()
print lst
                    
                
        
        