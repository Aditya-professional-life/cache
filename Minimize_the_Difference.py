import heapq as hq
from typing import List


class Solution:
    def minimizeDifference(self,n,k,arr):
        dic = {}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        


















        # max1 = max2 = float('-inf')
        # for i in arr:
        #     if i > max1:
        #         max2 = max1
        #         max1 = i
        #     elif max1 > i >max2:
        #         max2 = i

        # return (max1 - max2)


s1 = Solution()
n = 6
k = 3
arr = [2, 3, 1, 4, 6, 7]
result = s1.minimizeDifference(n,k,arr)
print(result)