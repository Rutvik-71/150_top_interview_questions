class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        
        word = s.split()

        reversed_string = word[::-1]

        return (' '.join(reversed_string))
        
#time complexity = O(n)
#space compexity = O(n)