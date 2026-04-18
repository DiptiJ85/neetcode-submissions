class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums)-1
        n1 = 0
        n2 = 0
        """
        while left<right:
            new_sum = nums[left] + nums[right]
            if new_sum == target:
                break
            elif new_sum < target:
                left+=1
            else:
                right-=1
        result = [left, right]
        """
        """
        result = {}
        for i, j in enumerate(nums):
            result[j] = i
        print(result)
        for n in range(len(nums)):
            print(n)
            num2 = target - nums[n]
            if num2 in result:
                n2indx = result[num2]
                if n!=n2indx:
                    n1 = n
                    n2 = n2indx
                    break
        print(n1, n2)
        return [n1,n2]
        """
        result = {}
        for indx, val in enumerate(nums):
            comple = target - val
            if comple in result:
                    return [result[comple],indx]
            result[val] = indx
        return result
