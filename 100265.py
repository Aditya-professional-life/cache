class Solution:
 
    def maximumPrimeDifference(self, nums):
        min_prime_idx, max_prime_idx = float('inf'), float('-inf')
        
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        for i, num in enumerate(nums):
            if is_prime(num):
                min_prime_idx = min(min_prime_idx, i)
                max_prime_idx = max(max_prime_idx, i)
        
        return max(max_prime_idx - min_prime_idx, 0)

nums = [4, 2, 9, 5, 3]
sol = Solution()
print(sol.maximumPrimeDifference(nums))  # Output should be 3
