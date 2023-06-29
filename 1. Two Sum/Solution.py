class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index=0
        index1=1
        for x in nums:
            for i in nums[1:]:
                if(i+x==target and not(index1==index)):
                    return [index,index1]
                index1+=1
            index1=1
            index+=1
        