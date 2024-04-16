class Solution:
    def findLatestTime(self, s: str) -> str:
        s = list(s)
        
        # If the first digit is "?", it can be "2" if the second digit is also "?" or less than "4", otherwise "1"
        if s[0] == "?":
            s[0] = "2" if s[1] == "?" or int(s[1]) <= 3 else "1"
        
        # If the second digit is "?", it can be "3" if the first digit is "2", otherwise "9"
        if s[1] == "?":
            s[1] = "3" if s[0] == "2" else "9"
        
        # If the third digit is "?", it can be "5"
        if s[3] == "?":
            s[3] = "5"
        
        # If the fourth digit is "?", it can be "9"
        if s[4] == "?":
            s[4] = "9"
        
        return "".join(s)

# Example usage:
solution = Solution()
print(solution.findLatestTime("1?:?4"))  # Output: "11:54"
print(solution.findLatestTime("0?:5?"))  # Output: "09:59"
