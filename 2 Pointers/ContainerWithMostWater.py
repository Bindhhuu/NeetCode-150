class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        area = 0

        while i<j:
            min_height= min(height[i], height[j])
            width = j-i
            area  =max(area, width* min_height)

            if height[i]< height[j]:
                i+=1
            else:
                j-=1
        return area
#tc: O(n)
#sc: O(1)        
