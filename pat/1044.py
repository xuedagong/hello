#coding=utf-8
'''
火星人是以13进制计数的：

地球人的0被火星人称为tret。
地球人数字1到12的火星文分别为：jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec。
火星人将进位以后的12个高位数字分别称为：tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou。
例如地球人的数字“29”翻译成火星文就是“hel mar”；而火星文“elo nov”对应地球数字“115”。为了方便交流，请你编写程序实现地球和火星数字之间的互译。

输入格式：

输入第一行给出一个正整数N（<100），随后N行，每行给出一个[0, 169)区间内的数字 —— 或者是地球文，或者是火星文。

输出格式：

对应输入的每一行，在一行中输出翻译后的另一种语言的数字。

输入样例：
4
29
5
elo nov
tam
输出样例：
hel mar
may
115
13
'''
#coding=utf-8
#判断一个字符是否 字母
def is_small_char(c):
    e=c[0]
    if ord(e)>=ord('a') and ord(e)<=ord('z'):
        return True
    return False
    
if __name__=="__main__":
    n=raw_input()
    map1=['tret','jan','feb','mar','apr','may','jun','jly','aug','sep','oct','nov','dec']
    map2=['tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']
    n=int(n)
    print_lst=[]
    for i in xrange(n):
        c=raw_input()
        if is_small_char(c):
            sum_int=0
            lst=c.split()
            if len(lst)==2:#2位
                sum_int= ( map2.index(lst[0])+1 )*13+map1.index(lst[1])
            else:
                if map2.index(lst[0])!=-1:
                    sum_int= (map2.index(lst[0])+1)*13
                else:
                    sum_int= map1.index(lst[0])
                    
            print_lst.append(sum_int)
        else:
            int_c=int(c)
            if int_c>=13:
                a1=int_c/13
                a2=int_c%13
                if a2>0:
                    print_lst.append( map2[a1-1]+" "+(map1[a2]) )
                else:
                    print_lst.append( map2[a1-1])
                   
            else:
                print_lst.append( map1[int_c]  )
    for item in  print_lst:
        print item
    exit(0)
            
                
            