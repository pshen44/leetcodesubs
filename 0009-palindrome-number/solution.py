class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        l, r = 0, len(x) - 1
        if x[l] == "-":
            return False
        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
        return True
