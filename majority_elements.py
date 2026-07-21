class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}

        # Count the frequency of each element
        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num] = 1

        # Find the majority element
        for key, value in dictionary.items():
            if value > len(nums) // 2:
                return key
    #time complexity = O(n)
    #space complexity = O(n)