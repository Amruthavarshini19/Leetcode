class Solution(object):
    def singleNumber(self, nums):
        l = []
        for num in nums:
            if nums.count(num)==1:
                l.append(num)
        return l
        