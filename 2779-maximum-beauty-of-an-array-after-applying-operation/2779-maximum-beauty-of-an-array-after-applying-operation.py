class Solution(object):
    def maximumBeauty(self, nums, k):
        nums.sort()
        l = 0
        ans = 0
        for r in range(len(nums)):
            while nums[r]-nums[l]>2*k:
                l+=1
            ans = max(ans, r-l+1)
        return ans
        