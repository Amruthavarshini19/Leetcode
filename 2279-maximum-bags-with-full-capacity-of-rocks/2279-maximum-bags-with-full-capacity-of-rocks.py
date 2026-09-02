class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        remaining = []
        for i in range(len(capacity)):
            remaining.append(capacity[i] - rocks[i])
        remaining.sort()
        answer = 0
        for need in remaining:
            if need > additionalRocks:
                break
            additionalRocks -= need
            answer += 1
        return answer
        