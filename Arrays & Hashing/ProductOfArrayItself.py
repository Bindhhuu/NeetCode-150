class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r_mult = 1
        l_mult = 1
        n = len(nums)
        r_arr = [0] * n
        l_arr = [0] * n

        for i in range(n):
            j = -i -1
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        
        return [l*r for l, r in zip(l_arr, r_arr)]
            #tc: O(n)
            #sc: O(n)
