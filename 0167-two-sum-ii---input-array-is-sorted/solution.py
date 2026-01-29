class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        wordmap = {} # word : index
        for idx, num in enumerate(numbers):
            diff = target - num
            if diff in wordmap:
                return [wordmap[diff] + 1, idx + 1]
            wordmap[num] = idx
