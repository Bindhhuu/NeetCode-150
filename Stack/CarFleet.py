class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(p, (target - p) / s) for p, s in zip(position, speed)]
        time.sort(reverse=True)
        fleet, curr = 0, 0

        for _, t in time:
            if t > curr:
                fleet += 1
                curr = t
        
        return fleet
