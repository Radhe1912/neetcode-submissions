class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        strs[:] = sorted(strs)
        l = len(strs[0])

        for i in range(l):
            if(strs[0][i]!=strs[-1][i]):
                break
            s+=strs[0][i]
        return s