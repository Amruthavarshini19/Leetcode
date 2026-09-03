class Solution(object):
    def fillCups(self, amount):
        t = sum(amount)
        l = max(amount)
        return max(l, (t+1)//2)
        