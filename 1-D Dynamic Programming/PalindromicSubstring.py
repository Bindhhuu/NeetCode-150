class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        def expand(l, r):
            nonlocal result #Whenever I update result inside expand, I want to change the result variable from the outer function countSubstrings, not create a new one.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                result += 1
                l -= 1
                r += 1

        for i in range(len(s)):
            expand(i, i)
            expand(i, i + 1)
        return result
