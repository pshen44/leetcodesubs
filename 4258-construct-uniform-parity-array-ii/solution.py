class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = False
        minOdd = float('inf')
        even = False
        for n in nums1:
            if n % 2 == 0:
                even = True
            else:
                odd = True
                minOdd = min(n, minOdd)
        if not odd or not even:
            return True
        for n in nums1:
            if n % 2 == 0 and n < minOdd:
                return False
        return True
