#coding=utf-8
'''
旧键盘上坏了几个键，于是在敲一段文字的时候，对应的字符就不会出现。现在给出应该输入的一段文字、以及实际被输入的文字，请你列出肯定坏掉的那些键。

输入格式：

输入在2行中分别给出应该输入的文字、以及实际被输入的文字。每段文字是不超过80个字符的串，由字母A-Z（包括大、小写）、数字0-9、以及下划线“_”（代表空格）组成。题目保证2个字符串均非空。

输出格式：

按照发现顺序，在一行中输出坏掉的键。其中英文字母只输出大写，每个坏键只输出一次。题目保证至少有1个坏键。

输入样例：
7_This_is_a_test
_hs_s_a_es
输出样例：
7TI
'''
a=raw_input()
b=raw_input()
b_index=0
a_index=0
err_lst=[]
while b_index<len(b):
    while a_index<len(a):
        if b[b_index]==a[a_index]:
            break
        else:
            mys=a[a_index]
            mys=mys.upper()
            if mys not in err_lst:
                err_lst.append(mys)
            a_index+=1
            
    b_index+=1
    a_index+=1
    

while a_index<len(a):
    mys=a[a_index]
    mys=mys.upper()
    if mys not in err_lst:
        err_lst.append(mys)
    a_index+=1
ss="".join(err_lst)
print ss.upper()
