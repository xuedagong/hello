#coding=utf-8
'''
题目描述
本题要求读入N名学生的成绩，将获得某一给定分数的学生人数输出。

输入描述:
输入在第1行给出不超过105的正整数N，即学生总人数。随后1行给出N名学生的百分制整数成绩，中间以空格分隔。最后1行给出要查询的分

数个数K（不超过N的正整数），随后是K个分数，中间以空格分隔。


输出描述:
在一行中按查询顺序给出得分等于指定分数的学生人数，中间以空格分隔，但行末不得有多余空格。

输入例子:
10
60 75 90 55 75 99 82 90 75 50
3 75 90 88

输出例子:
3 2 0
'''
if __name__ == '__main__':
    n=raw_input()
    lst=raw_input().split(" ")
    search_lst=raw_input().split(" ")
    dic={}
    for i in xrange(1,len(search_lst)):
        dic[  (search_lst[i]) ]=0
    for i in xrange(len(lst)):
        if lst[i] in dic:
            dic[ (lst[i])  ] +=1

    for i in xrange(1,len(search_lst)):
        print dic[  (search_lst[i]) ],

