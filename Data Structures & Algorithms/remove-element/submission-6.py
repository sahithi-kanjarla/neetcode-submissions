class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        self.nums = nums
        self.val = val
        count = 0

        for num in nums:
            if num != val:
                nums[count] = num
                count += 1

        return count

obj1 = Solution()
print(obj1.removeElement([0,1,2,2,3,0,4,2],2))

