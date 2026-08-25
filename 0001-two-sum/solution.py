class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in nmap:
                return [i, nmap[diff]]
            nmap[v] = i
