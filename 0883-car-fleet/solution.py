class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[p,s] for p, s in zip(position, speed)]
        stack = []
        for pos, spd in sorted(cars)[::-1]:
            timecar = (target - pos) / spd
            stack.append(timecar)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)

