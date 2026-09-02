class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        freq = Counter(arr)
        freqs = sorted(freq.values())
        unique = len(freqs)
        for count in freqs:
            if k>=count:
                k-=count
                unique-=1
            else:
                break
        return unique