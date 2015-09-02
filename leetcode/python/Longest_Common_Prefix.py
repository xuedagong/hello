#coding=utf-8
'''
Write a function to find the longest common prefix string amongst an array of strings.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        long_str=""
        long_index=0
        this_char=""
        while True:
            if long_index >= len(strs[0]):
                break
            out_break=False
            this_char=strs[0][long_index]
            for item in strs:
                if long_index >= len(item) :
                    out_break=True
                    break
                if  item[long_index]!=this_char :
                    out_break=True
                    break
            if out_break:
                break#需要跳出外层循环    
            long_index+=1
            long_str=long_str+this_char
        return long_str
# Solution().longestCommonPrefix([])
Solution().longestCommonPrefix(["abab","aba",""])

        
        
            
                    
            
            
        