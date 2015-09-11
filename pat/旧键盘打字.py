#coding=utf-8
'''
旧键盘上坏了几个键，于是在敲一段文字的时候，对应的字符就不会出现。现在给出应该输入的一段文字、以及坏掉的那些键，打出的结果文字会是怎样？

输入格式：

输入在2行中分别给出坏掉的那些键、以及应该输入的文字。其中对应英文字母的坏键以大写给出；每段文字是不超过105个字符的串。可用的字符包括字母[a-z, A-Z]、数字0-9、以及下划线“_”（代表空格）、“,”、“.”、“-”、“+”（代表上档键）。题目保证第2行输入的文字串非空。

注意：如果上档键坏掉了，那么大写的英文字母无法被打出。

输出格式：

在一行中输出能够被打出的结果文字。如果没有一个字符能被打出，则输出空行。

输入样例：
7+IE.
7_This_is_a_test.

7+IE.
7_This_is_a_test.
输出样例：
_hs_s_a_tst
_hs_s_a_tst
_hs_s_a_tst


qqaeYx16zZoU95
qqaeY16zZU95

XO
'''
#coding=utf-8
#判断一个字母是否是大写字母
def is_big_char(c):
    if ord(c)>=ord('A') and ord(c)<=ord("Z"):
        return True
    else:
        return False


if __name__ == '__main__':
    err_str=raw_input()
    err_lst=list(err_str)
    input_str=raw_input()
    shift_break=False
    if "+" in err_lst:
        shift_break=True
    out_str=""
    for one_c in input_str:
        no_output=False
        if shift_break and is_big_char(one_c):#上档键坏道了,而且是个大写字母
             #不可以输出
             no_output=True
        else:
            big_char=one_c.upper()
            if big_char in err_lst:
                #不可以输出
                no_output=True
        # print one_c,no_output
        # exit(0)
        if not no_output:
            out_str+=one_c
    print out_str
