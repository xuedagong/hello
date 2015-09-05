#coding=utf-8
'''
题目描述
给定区间[-2的31次方, 2的31次方]内的3个整数A、B和C，请判断A+B是否大于C。

输入描述:
输入第1行给出正整数T(<=10)，是测试用例的个数。随后给出T组测试用例，每组占一行，顺序给出A、B和C。整数间以空格分隔。


输出描述:
对每组测试用例，在一行中输出“Case #X: true”如果A+B>C，否则输出“Case #X: false”，其中X是测试用例的编号（从1开始）。

输入例子:
4

1 2 3

2 3 4

2147483647 0 2147483646

0 -2147483648 -2147483647

输出例子:
Case #1: false

Case #2: true

Case #3: true

Case #4: false
'''
if __name__ == '__main__':
    # print (2+3)>4
    # exit(0)
    n=raw_input() #一共需要输入多少的实例
    n=int(n)
    lst=[]
    for i in xrange(n):
        a,b,c=raw_input().split(" ")
        # print a,b,c
        a1=int(a)
        b1=int(b)
        c1=int(c)
        # print a1,b1,c1
        if (a1+b1)>c1:
            result="true"
        else:
            result="false"
        strs="Case #"+str(i+1)+": "+result
        lst.append(strs)
    for item in lst:
        print item




