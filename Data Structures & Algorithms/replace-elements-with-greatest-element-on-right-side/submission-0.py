class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        val = arr[-1]
        arr[-1] = -1

        for i in range(n-2, -1, -1):
            if val<arr[i]:
                temp = arr[i]
                arr[i] = val
                val = temp

            else:
                arr[i] = val

        return arr