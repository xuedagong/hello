#coding=utf-8
'''
题目描述
大家应该都会玩“锤子剪刀布”的游戏：

现给出两人的交锋记录，请统计双方的胜、平、负次数，并且给出双方分别出什么手势的胜算最大。

输入描述:
输入第1行给出正整数N（<=105），即双方交锋的次数。随后N行，每行给出一次交锋的信息，即甲、乙双方同时给出的的手势。C代表“锤子”、J代表“剪刀”、B代

表“布”，第1个字母代表甲方，第2个代表乙方，中间有1个空格。


输出描述:
输出第1、2行分别给出甲、乙的胜、平、负次数，数字间以1个空格分隔。第3行给出两个字母，分别代表甲、乙获胜次数最多的手势，中间有1个空格。如果解不唯

一，则输出按字母序最小的解。

输入例子:
10
C J
J B
C B
B B
B C
C C
C B
J B
B C
J J

输出例子:
5 3 2

2 3 5

B B
'''
#coding=utf-8
#根据a,b手势，返回相应的结果
#C> J >B >C
#0 表示 平
# 1表示a赢
#-1表示a输
def get_one_s(a,b):
    if a==b:
        return 0
    if a=="C":
        if b=='J':
            return 1
        elif b=='B':
            return -1
    elif a=="J":
        if b=='C':
            return -1
        elif b=='B':
            return 1
    elif a=="B":
        if b=='J':
            return -1
        elif b=='C':
            return 1

#根据一个数组返回其中出现次数最多的字母
def get_most_one(lst):
    if len(lst)==0:#为空数组
        return 'B'
    b_cnt,c_cnt,j_cnt=0,0,0
    max=0
    max_str=''
    for item in lst:
        if item=='B':
            b_cnt+=1
        elif item=='C':
            c_cnt+=1
        elif item=='J':
            j_cnt+=1
    if b_cnt>max:
        max=b_cnt
        max_str='B'
    if c_cnt>max:
        max=c_cnt
        max_str='C'
    if j_cnt>max:
        max=j_cnt
        max_str='J'
    return max_str




if __name__ == '__main__':
    n=raw_input()
    n=int(n)
    win,ping,lose=0,0,0
    a_win=[]
    b_win=[]
    for i in xrange(n):
        a,b=raw_input().split(" ")
        one_result=get_one_s(a,b)
        if one_result==0:
            ping+=1
        elif one_result==1:
            win+=1
            a_win.append(a)
        else:
            lose+=1
            b_win.append(b)
    print win,ping,lose
    print lose,ping,win
    print get_most_one(a_win),get_most_one(b_win)
