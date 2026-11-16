class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i,n in enumerate(nums):
            solution = target - n

            if solution in seen:
                return [seen[solution],i]
            else:
                seen[n] = i