class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, v in enumerate(temperatures):
            while stack and v > stack[-1][0]:
                tempVal, tempInd = stack.pop()
                res[tempInd] = i - tempInd
            stack.append([v,i])
        return res

