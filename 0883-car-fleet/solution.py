class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse = True)
        stack = []
        for pair in pairs:
            pos, speed = pair[0], pair[1]
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
