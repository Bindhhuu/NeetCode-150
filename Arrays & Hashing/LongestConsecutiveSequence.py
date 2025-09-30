class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in s:
            if i-1 not in s:
                nextt = i+1
                length = 1
                while nextt in s:
                    length +=1 
                    nextt +=1
                longest = max(longest, length)
        return longest
        #tc: O(n)
        #sc: O(n)
