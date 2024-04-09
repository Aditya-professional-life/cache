class Solution:
    def max_diff(self,arr):
        n = len(arr)
        max_diff = 0
        for i in range(n):
            for j in range(i+1,n):
                diff = arr[j] - arr[i]

                max_diff = max(max_diff,diff)



        return max_diff
    


s1 = Solution()
arr = [2,3,10,6,4,8,1]
result = s1.max_diff(arr)
print(result)
