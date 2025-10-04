class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, -num)

        max_left = -heapq.heappop(self.left)
        heapq.heappush(self.right, max_left)

        if len(self.right) > len(self.left):
            min_right = heapq.heappop(self.right)
            heapq.heappush(self.left, -min_right)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

#tc: O(log n) - add/psuh
# O(1) find med
#sc: O(n)
