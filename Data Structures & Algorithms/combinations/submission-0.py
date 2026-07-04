class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []

        def rec(i, al):
            if len(al)==k:
                arr.append(al[:])
                return
            if i>n:
                return
            al.append(i)
            rec(i+1, al)
            al.pop()
            rec(i+1, al)

        rec(1, [])
        return arr