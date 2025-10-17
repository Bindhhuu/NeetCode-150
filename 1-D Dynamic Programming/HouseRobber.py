class Solution:
    def rob(self, nums: List[int]) -> int:
        i = len(nums)

        if i == 1:
            return nums[0]
        if i == 2:
            return max(nums[0], nums[1])
                
        dp = [0] * i
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for n in range(2, i):
            dp[n] = max(nums[n] + dp[n-2], dp[n-1]) 
        return dp[i-1]

        '''
        #or
        i = len(nums)

        if i == 1:
            return nums[0]
        if i == 2:
            return max(nums[0], nums[1])

        prev = nums[0]
        curr = max(nums[0], nums[1])

        for n in range(2, i):
            prev, curr = curr, max(nums[n] + prev, curr)

        return curr
        '''
