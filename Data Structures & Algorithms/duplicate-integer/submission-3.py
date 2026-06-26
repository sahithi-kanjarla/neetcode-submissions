class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums

        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else: 
                return True
        return False