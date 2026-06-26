class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target

        summap = {}

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                summap[i,j] = nums[i] + nums[j]
                if summap[i,j] == target:
                    return [i,j]