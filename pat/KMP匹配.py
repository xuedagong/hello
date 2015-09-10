#coding=utf-8
'''
KMP匹配
跳过一部分已匹配字符
制作查询表，每次遇到一个失配条件，就查询失配位置的值并且移到对应位置。
如何制表？
只需要在失配的时候修改模式串中的位置j
而不需要修改文本串的位置i
制表：每一个字符对应一个匹配失败后的位置，在构造时，通过前置哨兵（值为-1），从0开始，i表示模式串，j表示匹配串，不妨这样考虑：
目前已经匹配到了i = n，即p[i] = j ,考虑n+1，如果 i = j+1 则令当前匹配j+1，且 p[++i] = ++j,如果不相等，则考虑p[p[i]] ，
这样递推下去，直到有相等的匹配。如果不，则会递推到哨兵即-1,这是p[++i] = ++j, 即等于首元素。

优化：当++i = ++j 时，直接跳过，直到不相等，因为如果相等相当于白白匹配，仍然不会匹配成功。


测试的用例：
主串 （S） ababcabcacbab  
子串 （T）abcac    
'''
#字符串查找，是否存在
#存在返回 位置 
#不存在 返回 False
def normal_search(strs,find_str):
    n=len(strs)
    find_lst=list(find_str)
    for i in xrange(n):
        if(strs[i]==find_str[0]):
            index_i=i+1
            j=1
            while j<len(find_lst) and index_i<n:
                if strs[index_i]==find_lst[j]:#配成功，继续
                    index_i+=1
                    j+=1
                else:#不成功
                    break
            if j==len(find_lst): #都匹配成功了
                return i
    return False

#KMP匹配
def kmp_search(strs,find_str):
    return
print normal_search("ababcabcacbab","abcac")
                     
            
