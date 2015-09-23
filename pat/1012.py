#coding=utf-8
'''
1012. 数字分类
给定一系列正整数，请按要求对数字进行分类，并输出以下5个数字：

A1 = 能被5整除的数字中所有偶数的和；
A2 = 将被5除后余1的数字按给出顺序进行交错求和，即计算n1-n2+n3-n4...；
A3 = 被5除后余2的数字的个数；
A4 = 被5除后余3的数字的平均数，精确到小数点后1位；
A5 = 被5除后余4的数字中最大数字。
输入格式：

每个输入包含1个测试用例。每个测试用例先给出一个不超过1000的正整数N，随后给出N个不超过1000的待分类的正整数。数字间以空格分隔。

输出格式：

对给定的N个正整数，按题目要求计算A1~A5并在一行中顺序输出。数字间以空格分隔，但行末不得有多余空格。

若其中某一类数字不存在，则在相应位置输出“N”。

输入样例1：
13 1 2 3 4 5 6 7 8 9 10 20 16 18
输出样例1：
30 11 2 9.7 9
输入样例2：
8 1 2 4 5 6 7 9 16
输出样例2：
N 11 2 N 9
'''
if __name__=="__main__":
    a1,a2,a3,a4,a5=0,0,0,0,0
    lst=map(int,raw_input().split() );
    new_lst=lst[1:]
    a2_cnt=0
    cnt=0
    flag=1
    test_lst=[]
    for item in new_lst:
        if item%5==0:
            if item%2==0:
                a1+=item
        elif item%5==1:
            a2+=flag*item
            flag=flag*(-1)
            a2_cnt+=1
        elif  item%5==2:
            a3+=1
        elif item%5==3:
            cnt+=1
            a4+=item
            test_lst.append(item)
        elif item%5==4:
            if item>a5:
                a5=item
    if a1==0:
        a1="N"
        
    if a2_cnt==0:
        a2="N"
        
    if a3==0:
        a3="N"
    
    if a4==0:
        a4="N"
    else:
        a4=round( a4*1.0/(cnt),1 )
    
    if a5==0:
        a5="N"
        
    print a1,a2,a3,a4,a5
        
            
            
            
        
    