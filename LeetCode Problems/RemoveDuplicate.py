class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        index = 0
        while(i < len(nums)-1):
            if(nums[i] == nums[i+1]):
                nums.pop(i+1)
                i-=1
            i+=1
        print(nums)
        print(index)
        
Solution().removeDuplicates([0,0,1,1,1,1,1,2,2,2,3,3,4])
    

                    
                    
                    
    