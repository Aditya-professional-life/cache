class Solution:
    def max_diff(self, arr):
        n = len(arr)
        res = arr[1] - arr[0]
        minval = arr[0]

        for j in range(1, n):
            res = max(res, arr[j] - minval)
            minval = min(arr[j], minval)

        return res

    def predict(self, arr):
        n = len(arr)
        profit = 0
        for i in range(n):
            for j in range(i+1, n):
                x = self.max_diff(arr[:j]) + self.max_diff(arr[j:])
                profit = max(profit, x)

        return profit

s1 = Solution()
arr = [1, 5, 3, 8, 12]
res = s1.predict(arr)
print(res)
