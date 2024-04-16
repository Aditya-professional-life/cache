from typing import List

class Solution:
    def minimizeDifference(self, n: int, k: int, arr: List[int]) -> int:
        arr.sort()
        min_diff = float('inf')
        for i in range(n - k + 1):
            min_diff = min(min_diff, arr[i + k - 1] - arr[i])
        return min_diff

s1 = Solution()

k = 3
arr = [2, 3, 1, 4, 6, 7]
n = len(arr)
result = s1.minimizeDifference(n, k, arr)
print(result)
