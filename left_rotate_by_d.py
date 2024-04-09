class Solution:
    def left_rotate(self,arr,x):
        n = len(arr)
        for i in  range(x):
            arr.append(arr.pop(0))

        return arr  

s1 = Solution()
arr = [1,2,3,4,5]
x = 2
result = s1.left_rotate(arr, x)
print(result)