from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        maxx = [-count for count in freq.values()]
        heapq.heapify(maxx)

        time = 0
        while maxx:
            temp = []
            cycle = n + 1

            for _ in range(cycle):
                if maxx:
                    count = heapq.heappop(maxx)
                    if count + 1 < 0:
                        temp.append(count + 1)
                time += 1
                if not maxx and not temp:
                    break
            
            for item in temp:
                heapq.heappush(maxx, item)

        return time
