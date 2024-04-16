class Solution:
    def pair_Sum(self, arr, n):
        left = 0
        right = n-1
        result = 0
        while left < right:
            # print(arr[left],arr[right])
            result += arr[left]&arr[right]
            right-=1
            if left  == right:
                left+=1
                right = n-1

        return result


s1 = Solution()

n = 4
arr = [10, 20, 30, 40]
result = s1.pair_Sum(arr,n)
print(result)