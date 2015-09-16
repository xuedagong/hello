#coding=utf-8
'''
题目描述
宋代史学家司马光在《资治通鉴》中有一段著名的“德才论”：“是故才德全尽谓之圣人，才德兼亡谓之愚人，德胜才谓之君子，才胜德谓之

小人。凡取人之术，苟不得圣人，君子而与之，与其得小人，不若得愚人。”



现给出一批考生的德才分数，请根据司马光的理论给出录取排名。

输入描述:
输入第1行给出3个正整数，分别为：N（<=105），即考生总数；L（>=60），为录取最低分数线，即德分和才分均不低于L的考生才有资格

被考虑录取；H（<100），为优先录取线——德分和才分均不低于此线的被定义为“才德全尽”，此类考生按德才总分从高到低排序；才分不到

但德分到线的一类考生属于“德胜才”，也按总分排序，但排在第一类考生之后；德才分均低于H，但是德分不低于才分的考生属于“才德兼

亡”但尚有“德胜才”者，按总分排序，但排在第二类考生之后；其他达到最低线L的考生也按总分排序，但排在第三类考生之后。


随后N行，每行给出一位考生的信息，包括：准考证号、德分、才分，其中准考证号为8位整数，德才分为区间[0, 100]内的整数。数字间以空格分隔。


输出描述:
输出第1行首先给出达到最低分数线的考生人数M，随后M行，每行按照输入格式输出一位考生的信息，考生按输入中说明的规则从高到低排序。当某类考生中有多人

总分相同时，按其德分降序排列；若德分也并列，则按准考证号的升序输出。

输入例子:
14 60 80
10000001 64 90
10000002 90 60
10000011 85 80
10000003 85 80
10000004 80 85
10000005 82 77
10000006 83 76
10000007 90 78
10000008 75 79
10000009 59 90
10000010 88 45
10000012 80 100
10000013 90 99
10000014 66 60

输出例子:
12

12
10000013 90 99
10000012 80 100
10000003 85 80
10000011 85 80
10000004 80 85
10000007 90 78
10000006 83 76
10000005 82 77
10000002 90 60
10000014 66 60
10000008 75 79
10000001 64 90
'''
#coding=utf-8
if __name__ == '__main__':
    lst1=[] #第一类考生 按照总分排名
    lst2=[] #第二类考生 德胜 才  总分排序
    lst3=[] #第三类  均低于H  德分不低于才分 按总分排序
    lst4=[]  #第四类  按照总分排序
    a,L,H=map(int, raw_input().split() )

    index=0
    cnt=0
    while  index<a:
        index+=1
        s1,d,c=raw_input().split()
        s1=int(s1)
        yueshu=s1%(a+1)
        d=int(d)
        c=int(c)
        total_lst=[]
        if d>=L and c>=L:
            cnt+=1
            if d>=H and c>=H:
                news=( (d+c)*100+d )*(a+1)+(yueshu)#占用了5位数字了
                lst1.append((s1,d,c,news))
            elif d>=H and c<H:
                news=( (d+c)*100+d )*(a+1)+(yueshu)#占用了5位数字了
                lst2.append((s1,d,c,news))
            elif d<H and c<H and d>=c:
                news=( (d+c)*100+d )*(a+1)+(yueshu)#占用了5位数字了
                lst3.append((s1,d,c,news))
            else:
                news=( (d+c)*100+d )*(a+1)+(yueshu)#占用了5位数字了
                lst4.append((s1,d,c,news))


    # lst2.sort(reverse=True)
    # lst3.sort(reverse=True)
    # lst4.sort(reverse=True)
    print cnt
    for item in sorted(lst1, key=lambda one_item: one_item[3],reverse=True):

        print item[0],item[1],item[2]

    for item in sorted(lst2, key=lambda one_item: one_item[3],reverse=True):

        print item[0],item[1],item[2]

    for item in sorted(lst3, key=lambda one_item: one_item[3],reverse=True):

        print item[0],item[1],item[2]

    for item in sorted(lst4, key=lambda one_item: one_item[3],reverse=True):

        print item[0],item[1],item[2]

    exit(0);
