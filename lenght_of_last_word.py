class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()      
        s = s[::-1]        

        ans = 0

        for ch in s:
            if ch == " ":
                break
            ans += 1

        return ans
    #time complexity = O(n)
    #space complexity = O(n)