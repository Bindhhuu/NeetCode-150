class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxx = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                hei = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxx = max(maxx, hei * width)

            stack.append(i)
        return maxx
