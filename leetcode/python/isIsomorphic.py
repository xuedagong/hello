class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        maps={}
        maps2={}
        s_lst=list(s)
        for i in range(len(s_lst)):
            map_key=t[i]
            map_key2=s_lst[i]
            map_val=ord( s_lst[i] )- ord(t[i])
            if map_key in maps:
                if map_val!=maps[map_key]:
                    return False
            else:
                maps[map_key]=map_val

            if map_key2 in maps2:
                if map_val!=maps2[map_key2]:
                    return False
            else:
                maps2[map_key2]=map_val
        return True
print Solution().isIsomorphic("egg","add" )
print Solution().isIsomorphic("foo","bar" )
print Solution().isIsomorphic("paper","title" )

