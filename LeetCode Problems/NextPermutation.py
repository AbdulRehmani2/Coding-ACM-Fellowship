def LargestElement(nums: list[int]):
    num = nums.copy()
    num.sort()
    return num[-1]

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        largest = LargestElement(nums)
        i = 0
        while(i < len(nums)):
            if(len(nums) == 2):
                nums[0], nums[1] = nums[1], nums[0]
                return
            if(nums[0] == largest):
                Solution().nextPermutation(nums[1:])
            elif(nums[i] == largest):
                nums[i], nums[i-1] = nums[i-1], nums[i]
            i+=1
        print(nums)

Solution().nextPermutation([3, 1, 2])