class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = nums[0]
        minn = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            if n < 0:
                minn, maxx = maxx, minn  
            
            maxx = max(n, n*maxx)
            minn = min(n, n*minn)
            res = max(res, maxx)
        
        return res
