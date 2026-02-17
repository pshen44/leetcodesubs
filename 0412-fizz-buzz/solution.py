class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for num in range(1, n + 1):
            res = ""
            if num % 3 == 0:
                res += "Fizz"
            if num % 5 == 0:
                res += "Buzz"
            if not res:
                res += str(num)
            out.append(res)
        return out
