class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        see={}
        for i,n in enumerate(nums):
            ned=target-n
            if ned in see:
                return[see[ned],i]
            see[n]=i

