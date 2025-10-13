class Solution:
    from collections import deque
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minute = 0
        q = deque()
        freshcount = 0
        M, N = len(grid), len(grid[0])

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    freshcount += 1

        while q and freshcount > 0:
            rotting = len(q)
            for _ in range(rotting):
                i, j = q.popleft()
                for r, c in [(i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)]:
                    if 0 <= r < M and 0 <= c < N and grid[r][c] == 1:
                        grid[r][c] = 2
                        freshcount -= 1
                        q.append((r, c))
            minute += 1
        return minute if freshcount == 0 else -1
