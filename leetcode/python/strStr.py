'''
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lens=len(haystack)
        if needle=='' :
            return 0
        if needle=='' or haystack=='':
            return -1
        if lens<len(needle):
            return -1
        
        i=0
        while i <= lens-len(needle):
            if haystack[i]==needle[0]:
                m,n=i,0
                
                while  m<lens and n<len(needle):
                    if haystack[m]==needle[n]:
                        m+=1
                        n+=1
                    else:
                        break
                if n==len(needle):
                    return i
                i=i+1 
            else:
                i=i+1 
        return -1
#
print Solution().strStr("mississippi", "issip")            
                
                
                    
                     
        