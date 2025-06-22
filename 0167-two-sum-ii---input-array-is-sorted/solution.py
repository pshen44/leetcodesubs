class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        num = None
        while target != num:
            num = numbers[l] + numbers[r]
            if target == num:
                break
            if target < num:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]
                
