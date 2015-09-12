#coding=utf-8
'''
请编写程序，找出一段给定文字中出现最频繁的那个英文字母。

输入格式：

输入在一行中给出一个长度不超过1000的字符串。字符串由ASCII码表中任意可见字符及空格组成，至少包含1个英文字母，以回车结束（回车不算在内）。

输出格式：

在一行中输出出现频率最高的那个英文字母及其出现次数，其间以空格分隔。如果有并列，则输出按字母序最小的那个字母。统计时不区分大小写，输出小写字母。

输入样例：
This is a simple TEST.  There ARE numbers and other symbols 1&2&3...........
输出样例：
e 7
'''
#coding=utf-8
def is_char(c):
    if ord(c)>=ord('a') and ord(c)<=ord("z"):
        return True
    else:
        return False
if __name__ == '__main__':
    str1=raw_input()
    max_key=''
    max_val=0
    dicts={}
    for c in str1:
        c=c.lower()
        if not is_char(c):
            continue

        if c in dicts:
            dicts[c]+=1
        else:
            dicts[c]=1
    keys= dicts.keys()
    keys.sort()
    for one_key in keys:
        if dicts[one_key]>max_val:
            max_key=one_key
            max_val=dicts[one_key]
    print max_key,max_val



