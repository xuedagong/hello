#coding=utf-8
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.strip()
        sum=0
        flags=0

        for i in xrange(len(str)):
            item=str[i]

            one_int=self.onestr_to_int(item)
            if one_int==-1:
                if i>0:
                    break
                if item=="-":
                    flags=1
                if item!='-' and item!='+':
                    break

                continue
            else:
                sum=sum*10+self.onestr_to_int(item)

        if flags==1:
            sum=-sum
        if sum>2147483647:
            sum=2147483647
        if sum<-2147483648:
            sum=-2147483648
        return sum



    def onestr_to_int(self,str):
        if str=='0' :
            return 0
        elif str=='1':
            return 1
        elif str=='2':
            return 2
        elif str=='3':
            return 3
        elif str=='4':
            return 4
        elif str=='5':
            return 5
        elif str=='6':
            return 6
        elif str=='7':
            return 7
        elif str=='8':
            return 8
        elif str=='9':
            return 9
        else:
            return -1

if __name__ == '__main__':
    print Solution().myAtoi(" b11228552307")
