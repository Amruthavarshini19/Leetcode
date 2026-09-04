class Solution(object):
    def partition(self, s):
        r = []
        def palindrome(l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        def backtrack(start, current):
            if start==len(s):
                r.append(current[:])
                return
            for end in range(start, len(s)):
                if palindrome(start, end):
                    current.append(s[start:end+1])
                    backtrack(end+1, current)
                    current.pop()
        backtrack(0, [])
        return r

        