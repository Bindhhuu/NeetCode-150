class Solution:
    def solve(self, nums):
        n = len(nums)
        prev = nums[0]
        prev2 = 0

        for i in range(1, n):
            pick = nums[i] + (prev2 if i > 1 else 0)
            nonPick = prev
            curr = max(pick, nonPick)
            prev2 = prev
            prev = curr

        return prev

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        arr1 = nums[1:]      
        arr2 = nums[:-1]     
        return max(self.solve(arr1), self.solve(arr2))
