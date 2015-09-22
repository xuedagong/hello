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

if __name__ == '__main__':
    n=raw_input()
    n=int(n)
    win,ping,lose=0,0,0
    a_win=[]
    b_win=[]
    a_c,a_j,a_b=0,0,0
    
    
    
    
    b_c,b_j,b_b=0,0,0
    for i in xrange(n):
        a,b=raw_input().split()
        if a==b:
            ping+=1
        elif ( a=='C' and b=='J' )  :
            win+=1
            a_c+=1
        elif ( a=='J' and b=='B' ) :
            win+=1
            a_j+=1
        elif ( a=='B' and b=='C' ) :
            win+=1
            a_b+=1
            
        elif ( a=='J' and b=='C' )  :
            lose+=1
            b_c+=1
        elif ( a=='B' and b=='J' )  :
            lose+=1
            b_j+=1
        elif ( a=='C' and b=='B' ) :
            lose+=1
            b_b+=1
     
    a_max_str='B'
    a_max=a_b
    
    b_max_str='B'
    b_max=b_b
    
    if a_c>a_max:
        a_max=a_c
        a_max_str='C'
    
    if a_j>a_max:
        a_max=a_j
        a_max_str='J'
        
    if b_c>b_max:
        b_max=a_c
        b_max_str='C'
    
    if b_j>b_max:
        b_max=b_j
        b_max_str='J'
        
    print win,ping,lose
    print lose,ping,win
    print a_max_str,b_max_str
