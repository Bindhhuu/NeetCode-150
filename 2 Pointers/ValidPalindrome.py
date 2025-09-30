class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char.lower() for char in s if char.isalnum())
        i=0
        j=len(clean)-1
        while i<j:
            if clean[i] != clean[j]:
                return False
            i+=1
            j-=1
        return True
#TC: O(n)
#SC: O(1)
