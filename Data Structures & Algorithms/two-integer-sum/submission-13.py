class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for indx, val in enumerate(nums):
            comple = target - val
            if comple in result:
                    return [result[comple],indx]
            result[val] = indx
        return result
