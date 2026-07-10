class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = threshold*k
        s = sum(arr[:k])
        count = 0

        if s>=target:
            count+=1

        for i in range(k, len(arr)):
            s+=arr[i]
            s-=arr[i-k]

            if s>=target:
                count+=1

        return count