class Solution(object):
    def twoSum(self, nums, target):

        seen={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]]=i
        
        """
        seen=set()
        for num in nums:
            complement=target-num
            if complement in seen:
                return [complement,num]
            seen.add(num)   
        """