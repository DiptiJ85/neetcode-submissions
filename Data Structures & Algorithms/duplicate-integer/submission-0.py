class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasD  = False
        result = {}
        counter = 0
        for n in nums:
            if n not in result:
                result[n] = 1
            else:
                hasD = True
        return hasD
