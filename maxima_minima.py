class Solution:
    def max_profit(self,arr,n):
        profit = 0
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                profit += arr[i] - arr[i-1]

        return profit


# Test case 1: Normal case
arr = [1, 5,  3, 8, 12]
n = len(arr)
solution1 = Solution()
result =solution1.max_profit(arr,n)
print(result)