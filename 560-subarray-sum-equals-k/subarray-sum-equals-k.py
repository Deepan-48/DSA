class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        freq={0:1}
        curr_sum=0
        count=0
        for num in nums:
            curr_sum+=num
            rem=curr_sum-k
            if rem in freq:
                count+=freq[rem]
            if curr_sum in freq:
                freq[curr_sum]+=1
            else:
                freq[curr_sum]=1
        return count
        