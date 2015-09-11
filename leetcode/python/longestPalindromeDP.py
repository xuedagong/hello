#coding=utf-8
'''
Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

'''
string longestPalindromeDP(string s) {
  int n = s.length();
  int longestBegin = 0;
  int maxLen = 1;
  bool table[1000][1000] = {false};
  for (int i = 0; i < n; i++) {
    table[i][i] = true;
  }
  for (int i = 0; i < n-1; i++) {
    if (s[i] == s[i+1]) {
      table[i][i+1] = true;
      longestBegin = i;
      maxLen = 2;
    }
  }
  for (int len = 3; len <= n; len++) {
    for (int i = 0; i < n-len+1; i++) {
      int j = i+len-1;
      if (s[i] == s[j] && table[i+1][j-1]) {
        table[i][j] = true;
        longestBegin = i;
        maxLen = len;
      }
    }
  }
  return s.substr(longestBegin, maxLen);
}
'''
class Solution(object):
    def longestPalindrome(self, s):
        s_lst=list(s)
        n=len(s_lst)
        
        longestBegin = 0
        maxlen = 1
        table=[]
        for i in xrange(1000):
            one_table=[]
            for i in xrange(1000):
                one_table.append(False)
            table.append(one_table)
        
        for  i in xrange(1000):
            table[i][i]=True
        for i in xrange(n-1):
            if s[i]==s[i+1]:
                table[i][i+1] = True
                longestBegin = i
                maxLen = 2
        for lens in xrange(3,n+1):
            for i in xrange(0,n-lens+1):
                j=i+lens-1
                if s[i]==s[j] and table[i+1][j-1]:
                    table[i][j]=True
                    longestBegin = i
                    maxlen=lens
        return s[longestBegin:(longestBegin+maxlen)]
if __name__ == '__main__':
    print Solution().longestPalindrome("aaabaaaa")
            
    