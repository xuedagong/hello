#coding=utf-8
'''
1002. 写出这个数 (20)

时间限制
400 ms
内存限制
65536 kB
代码长度限制
8000 B
判题程序
Standard
作者
CHEN, Yue
读入一个自然数n，计算其各位数字之和，用汉语拼音写出和的每一位数字。

输入格式：每个测试输入包含1个测试用例，即给出自然数n的值。这里保证n小于10100。

输出格式：在一行内输出n的各位数字之和的每一位，拼音数字间有1 空格，但一行中最后一个拼音数字后没有空格。

输入样例：
1234567890987654321123456789
输出样例：
yi san wu
'''
#根据一个数字返回其汉语读音
def get_han(i):
    if i=='0':
        return 'ling'
    elif i=='1':
        return 'yi'
    elif i=='2':
        return 'er'
    elif i=='3':
        return 'san'
    elif i=='4':
        return 'si'
    elif i=='5':
        return 'wu'
    elif i=='6':
        return 'liu'
    elif i=='7':
        return 'qi'
    elif i=='8':
        return 'ba'
    elif i==9:
        return 'jiu'
    else:
        return ''

if __name__ == '__main__':
    s=raw_input()
    sum=0
    for item in s:
        if item=='-':
            continue
        else:
            sum+=int(item)
    sum=str(sum)
    lst=[]
    for item in sum:
        print get_han(item),
    exit(0)
    # print " ".join(lst)

