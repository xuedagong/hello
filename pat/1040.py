#coding=utf-8
'''
字符串APPAPT中包含了两个单词“PAT”，其中第一个PAT是第2位(P),第4位(A),第6位(T)；第二个PAT是第3位(P),第4位(A),第6位(T)。

现给定字符串，问一共可以形成多少个PAT？

输入格式：

输入只有一行，包含一个字符串，长度不超过105，只包含P、A、T三种字母。

输出格式：

在一行中输出给定字符串中包含多少个PAT。由于结果可能比较大，只输出对1000000007取余数的结果。

输入样例：
APPAPT
输出样例：
2
'''
'''
把pat 出现的位置保存起来,然后对比统计
'''

strs=raw_input()
p_lst=[]
a_lst=[]
t_lst=[]
for i in xrange(len(strs)):
    item=strs[i]
    if item=='P':
        p_lst.append(i)
    elif item=="A":
        a_lst.append(i)
    elif item=='T':
        t_lst.append(i)
cnt=0
a_len=len(a_lst)
t_len=len(t_lst)

if len(p_lst)>0 and len(a_lst)>0 and len(t_lst)>0:
    start_a=0
    start_t=0
    for one_p in p_lst:
        
        for a_index in xrange(start_a,a_len):
            if a_lst[a_index]<one_p:
                start_a=a_index
            else:
                for t_index in xrange(start_t,t_len):
                    if t_lst[t_index]<a_lst[a_index]:
                        start_t=t_index
                    else:
                        cnt+=1
                    
print cnt