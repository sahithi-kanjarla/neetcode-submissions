class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        self.nums = nums
        ans = []
        n = len(nums)
        for i in range(len(nums)):
            ans.append(nums[i])
        ans.extend(nums)
        return ans 
        