// Last updated: 3/20/2025, 6:20:59 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:   # already filtered
            return len(nums)
       
        
        curr_num = nums[0]
        i = 1
        safe_i = 0  # safe index to replace
        while i < len(nums):
            if nums[i] <= curr_num:
                nums[safe_i] = nums[i]
                if curr_num == nums[-1]:    # all uniques found
                    break
                i += 1
            else:
                curr_num = nums[i]
                safe_i += 1
                
        return safe_i + 1