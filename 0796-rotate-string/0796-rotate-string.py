class Solution(object):
    def rotateString(self, s, goal):
        if len(s)!=len(goal):
            return False
        if s==goal:
            return True
        for i in range(len(s)):
            if s[i:]+s[:i]==goal:
                return True
        return False
        