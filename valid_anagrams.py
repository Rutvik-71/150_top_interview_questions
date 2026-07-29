class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If lengths are different, they can't be anagrams
        if len(s) != len(t):
            return False

        hashmap = {}

        # Count the frequency of each character in s
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        # Decrease the frequency using characters from t
        for char in t:
            if char not in hashmap:
                return False

            hashmap[char] -= 1

            if hashmap[char] < 0:
                return False

        return True
    #time complexity =O(n)
    #space  complexity = O(1)