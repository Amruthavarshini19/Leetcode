class Solution(object):
    def partitionLabels(self, s):
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        start = 0
        end = 0
        r = []
        for i in range(len(s)):
            end = max(end, last[s[i]])
            if i==end:
                r.append(i-start+1)
                start = i+1
        return r
        