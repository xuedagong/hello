#coding=utf-8

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        while version1!='' or version2!='':
            n1=self.get_now_version(version1)
            n2=self.get_now_version(version2)
            find1=self.get_now_version_index(version1)
            find2=self.get_now_version_index(version2)
            # print n1,n2
            if n1>n2:
                return 1
            elif n1<n2:
                return -1

            if find1 >-1:
                version1=version1[find1+1:]
            else :
                version1=''

            if find2 >-1:
                version2=version2[find2+1:]
            else:
                version2=''
        return 0



    #获取当前的版本数字
    def get_now_version(self,version):
        find_index=version.find(".")
        if find_index>=0:
            return int( version[:find_index] )
        if version!='':
            return int(version)
        return 0
    def get_now_version_index(self,version):
        find_index=version.find(".")
        return find_index




if __name__ == '__main__':
    print Solution().compareVersion("1", "1.1")
