#coding=utf-8
'''
题目描述
大侦探福尔摩斯接到一张奇怪的字条：“我们约会吧！ 3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm”。大侦探很

 快就明白了，字条上奇怪的乱码实际上就是约会的时间“星期四 14:04”，因为前面两字符串中第1对相同的大写英文字母（大小写有区分）是

 第4个字母'D'，代表星期四；第2对相同的字符是'E'，那是第5个英文字母，代表一天里的第14个钟头（于是一天的0点到23点由数字0到9、

 以及大写字母A到N表示）；后面两字符串第1对相同的英文字母's'出现在第4个位置（从0开始计数）上，代表第4分钟。现给定两对字符串，

 请帮助福尔摩斯解码得到约会的时间。

输入描述:
输入在4行中分别给出4个非空、不包含空格、且长度不超过60的字符串。


输出描述:
在一行中输出约会的时间，格式为“DAY HH:MM”，其中“DAY”是某星期的3字符缩写，即MON表示星期一，TUE表示星期二，WED表示星期三，THU表示星期

四，FRI表示星期五，SAT表示星期六，SUN表示星期日。题目输入保证每个测试存在唯一解。

输入例子:
3485djDkxh4hhGE
2984akDfkkkkggEdsb
s&hgsfdk
d&Hyscvnm

输出例子:
THU 14:04
'''
#根据字母来获取星期
def get_week(s):
    if s=='A':
        return 'MON'
    elif s=='B':
        return 'TUE'
    elif s=='C':
        return 'WED'
    elif s=='D':
        return 'THU'
    elif s=='E':
        return 'FRI'
    elif s=='F':
        return 'SAT'
    elif s=='G':
        return 'SUN'

def get_hour(s):
    if ord(s)>=48 and ord(s)<57:
        return "0"+s
    else:
        return str( 10+ord(s)-ord("A") )
#判断一个字符是否是大写字母
def isBigchar(s):
    if ord(s)>=ord("A") and ord(s) <=ord("Z"):
        return True
    else:
        return False
#判断一个字母是否是英文字母
def isEngchar(s):
    if ord(s)>=ord("A") and ord(s) <=ord("Z"):
        return True
    elif ord(s)>=ord("a") and ord(s) <=ord("z"):
        return True
    else:
        return False


if __name__ == '__main__':
    s1=raw_input()
    s2=raw_input()
    s3=raw_input()
    s4=raw_input()
    a1=''
    j=0
    for i in xrange(len(s1)):
        if s1[i]==s2[i]:
            if j==1:
                j+=1
            if j==2:#第二个相同的字符
                a2=s1[i]
                break

            if isBigchar(s1[i]) and a1=='':
                a1=s1[i]
                j+=1
    for i in xrange(len(s3)):
        if s3[i]==s4[i]:
            if isEngchar( s3[i] ):
                if i<10:
                    a3='0'+str(i)
                else:
                    a3=str(i)

                break

    print get_week(a1)+" "+get_hour(a2)+':'+a3





