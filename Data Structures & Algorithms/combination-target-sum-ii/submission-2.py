class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        arr = []

        def rec(al, i, s):
            if s==target:
                arr.append(al[:])
                return
            if i>=n or s>target or candidates[i]>target-s:
                return
            al.append(candidates[i])
            rec(al, i+1, s+candidates[i])
            al.pop()

            j = i
            while j+1<n and candidates[j]==candidates[j+1]:
                j+=1
            rec(al, j+1, s)

        rec([], 0, 0)
        return arr