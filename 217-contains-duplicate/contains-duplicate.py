class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for num in nums:
            if freq[num]>1:
                return True
        return False

        """
        check=set()
        if len(check)==len(nums):
            return False
        else:
            return True
        """