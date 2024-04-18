class Solution:
    def max_profit_once(self,arr,n):
        '''keep track of min value and max profit'''
        mn , profit = arr[0] , float('-inf')
        for i in arr:
            profit = max(profit,i - mn)
            mn = min(mn , i)
        print(f"The maxium profit after buying 1 stock is : {profit}")

        
    def max_profit(self ,arr, n):
        '''more than 1 transctions
            is possible keep trrack of profit only
            check with prevouis element'''
        profit = 0
        for i in range(1,n):
            if arr[i] >arr[i-1]:
                profit+= arr[i] - arr[i-1]

        print(f"The maxium profit earned is {profit}")

            
    def max_profit_days(self, arr, n):
        ans = []
        i,j = 0,1
        n = len(arr)

        while j < n:
            if arr[j] > arr[j-1]:
                j+=1
                if j==n:
                    ans.append([i,j-1])
            else:
                if j-i >1:
                    ans.append([i,j-1])

                i= j
                j+=1 

        print(ans)







s1 = Solution()
arr = [7,1,5,3,6,4]
n = len(arr)
s1.max_profit_once(arr,n)
s1.max_profit(arr,n)
s1.max_profit_days(arr,n)