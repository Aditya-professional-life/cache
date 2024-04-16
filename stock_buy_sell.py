class Solution:
    def maxProfit(self, arr, start, end):
        if end <= start:
            return 0
        res = 0
        for i in range(start, end):
            for j in range(i + 1, end + 1):
                if arr[j] > arr[i]:
                    curr = (arr[j] - arr[i]) + self.maxProfit(arr, 0, i - 1) + self.maxProfit(arr, j + 1, end)
                    res = max(res, curr)
        return res

s1 = Solution()
arr = [1, 5, 3, 8, 12]
res = s1.maxProfit(arr, 0, 4)
print(res)
