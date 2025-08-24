class Solution:
    def isHappy(self, n: int) -> bool:
        cycle = set()
        while n != 1:
            prod = []
            for digit in str(n):
                prod.append(int(digit) * int(digit))
            n = sum(prod)
            if n in cycle:
                return False
            cycle.add(n)
            print(cycle)
        return True

