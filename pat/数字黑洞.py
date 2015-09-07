#coding=utf-8
'''
题目描述
给定任一个各位数字不完全相同的4位正整数，如果我们先把4个数字按非递增排序，再按非递减排序，然后用第1个数字减第2个数字，将得到

一个新的数字。一直重复这样做，我们很快会停在有“数字黑洞”之称的6174，这个神奇的数字也叫Kaprekar常数。



例如，我们从6767开始，将得到



7766 - 6677 = 1089

9810 - 0189 = 9621

9621 - 1269 = 8352

8532 - 2358 = 6174

7641 - 1467 = 6174

... ...



现给定任意4位正整数，请编写程序演示到达黑洞的过程。

输入描述:
输入给出一个(0, 10000)区间内的正整数N。


输出描述:
如果N的4位数字全相等，则在一行内输出“N - N = 0000”；否则将计算的每一步在一行内输出，直到6174作为差出现，输出格式见样例。注意每个数字按4位数格

式输出。

输入例子:
6767

输出例子:
7766 - 6677 = 1089
9810 - 0189 = 9621
9621 - 1269 = 8352
8532 - 2358 = 6174
'''

#coding=utf-8
#解题思路，就是没有解题思路，直接按照描述来求解
#根据4位strs 打印过程
def get_print(strs):
    str_lst=list(strs)
    str_lst.sort(reverse=True)
    a1="".join(str_lst)
    str_lst.sort()
    a2="".join( str_lst )
    int1=int(a1)
    int2=int(a2)
    if int1==int2:
        print a1+" - "+a2+" = 0000"
        return
    elif int1-int2==6174 :
        print a1+" - "+a2+" = 6174"
        return
    else:
        print a1+" - "+a2+" = "+str(int1-int2)
        return get_print(str(int1-int2))
if __name__ == '__main__':

    strs=raw_input()
    if len(strs)<4:
        for i in xrange(len(strs),4):
            strs+='0'

    get_print(strs)
