class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        count = [0]*26
        
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]+=1
            count[ord(t[i])-ord('a')]-=1

        for val in count:
            if val!=0:
                return False
        
        return True

        # map1 = {}
        # map2 = {}

        # if len(s)!=len(t):
        #     return False

        # for i in range(len(s)):
        #     map1[s[i]] = map1.get(s[i],0)+1

        # for i in range(len(t)):
        #     map2[t[i]] = map2.get(t[i],0)+1

        # for i in range(len(s)):
        #     if map1.get(s[i])!=map2.get(s[i]):
        #         return False
                
        # return True

        # return collections.Counter(s) == collections.Counter(t)