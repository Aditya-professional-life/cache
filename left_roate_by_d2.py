class Solution:
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
        return arr
    
    def left_rotate(self, arr, d):

        arr[:d] = self.reverse(arr, 0, d - 1)
        arr[d:] = self.reverse(arr, d, len(arr) - 1)
        arr[:] = self.reverse(arr, 0, len(arr) - 1)  # Reversing the entire array
        return arr

s1 = Solution()
arr = [1, 2, 3, 4, 5, 6]
d = 3
result = s1.left_rotate(arr, d)
print(result)


