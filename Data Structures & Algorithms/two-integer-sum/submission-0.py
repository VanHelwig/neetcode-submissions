class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            solution = target - num
        
            if solution in seen:
                return [seen[solution], i]

            seen.update({num: i})