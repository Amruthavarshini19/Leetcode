class Solution(object):
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []
        count = Counter(changed)
        result = []
        for x in sorted(count):
            if count[x] == 0:
                continue
            if x == 0:
                if count[x] < 2:
                    return []
                pairs = count[x] // 2
                result.extend([0] * pairs)
                count[x] = 0
                continue
            if count[2 * x] < count[x]:
                return []
            result.extend([x] * count[x])
            count[2 * x] -= count[x]
            count[x] = 0
        return result
        