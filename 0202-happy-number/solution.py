class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        while n != 1:
            prod = []
            for dig in str(n):
                prod.append(int(dig) * int(dig))
            n = sum(prod)
            if n in cycle:
                return False
            cycle.add(n)
        return True
