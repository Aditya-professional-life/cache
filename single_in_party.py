
class Solution:
    def findSingle(self, n, arr):
        d = {}
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        print(d)
        for i in d.keys():
            if d[i] == 1:
                return i

    
s1 = Solution()
n = 13
arr = [1 ,2, 3, 5, 3, 2, 1, 4, 5, 6, 6, 4, 4]
result = s1.findSingle(n,arr)
print(result)
