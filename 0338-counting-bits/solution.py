class Solution:
    def countBits(self, n: int) -> List[int]:
        i = 0
        res = []
        for num in range(n + 1):
            count = 0
            for i in range(32):
                if num & (1 << i):
                    count += 1
                print(count)
            res.append(count)
        return res


