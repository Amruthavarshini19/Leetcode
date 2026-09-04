class Solution(object):
    def subsets(self, nums):
        r = []
        def backtrack(index,current):
            r.append(current[:])
            for i in range(index, len(nums)):
                current.append(nums[i])
                backtrack(i+1,current)
                current.pop()
        backtrack(0, [])
        return r
        