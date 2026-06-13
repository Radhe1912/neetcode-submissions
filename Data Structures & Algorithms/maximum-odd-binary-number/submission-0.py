class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        hm = Counter(s)
        one = hm['1']
        zero = hm['0']
        ans = ""
        while one>1:
            ans+='1'
            one-=1
        while zero!=0:
            ans+='0'
            zero-=1
        ans+='1'
        return ans