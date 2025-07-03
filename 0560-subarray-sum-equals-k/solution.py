class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefmap = {0 : 1}
        currSum = 0
        res = 0
        for num in nums:
            currSum += num
            pref = currSum - k
            if pref in prefmap:
                res += prefmap.get(pref)
            if currSum in prefmap:
                prefmap[currSum] += 1
            else:
                prefmap[currSum] = 1
        return res

