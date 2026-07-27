class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(ch.lower() for ch in s if ch.isalnum())

        if result == result[::-1]:
            return True
        else:
            return False
        #time complexity = O(n)
        #space complexity = O(n)