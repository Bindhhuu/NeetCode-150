class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L =0
        R= len(nums)-1

        while L <=R:
            M = (L+R)//2

            if nums[M] == target:
                return M

            elif target < nums[M]:
                R = M-1

            else:
                L = M+1
        return -1
