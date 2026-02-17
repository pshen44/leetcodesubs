class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            res = 0
            for dig in str(num):
                res += int(dig)
            num = res
        return num
        
