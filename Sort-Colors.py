class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        oldNums = nums[:]
        nums.clear()  

        for i in range(len(oldNums)):
            inserted = False
            for ii in range(len(nums)):
                if oldNums[i] < nums[ii]:
                    nums.insert(ii, oldNums[i])
                    inserted = True
                    break
            if not inserted: nums.append(oldNums[i])
        