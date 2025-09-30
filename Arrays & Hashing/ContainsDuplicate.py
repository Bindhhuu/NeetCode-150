class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = set()

        for num in nums:
            if num in n:
                return True
            n.add(num)    
        return False
      #TC: O(n)
      #SC: O(n)
