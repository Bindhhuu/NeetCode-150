class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    out.append(i)
                    out.append(j)
                else:
                    j +=1
            i += 1

        return out
#TC: O(n)
#SC: O(n)
