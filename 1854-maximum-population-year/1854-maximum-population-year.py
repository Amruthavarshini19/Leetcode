class Solution(object):
    def maximumPopulation(self, logs):
        mp = 0
        ans = 1950
        for year in range(1950,2051):
            p = 0
            for birth , death in logs:
                if birth<=year<death:
                    p+=1
            if p>mp:
                mp=p
                ans=year
        return ans


        