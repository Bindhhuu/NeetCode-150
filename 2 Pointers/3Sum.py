class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = set()
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return [list(triplet) for triplet in result]

#TC: O(n²)
#SC: O(1)
