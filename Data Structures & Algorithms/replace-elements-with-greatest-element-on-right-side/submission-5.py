class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        self.arr = arr
        count = 0
        last = len(arr) - 1

        for num in range(len(arr)):
            if num < last:
                arr[count] = max(arr[num+1:])
                count+=1
            if num == last:
                arr[last] = -1
        return arr

        