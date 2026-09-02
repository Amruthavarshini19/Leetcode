class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        valid = []
        for r in restaurants:
            if (veganFriendly == 0 or r[2] == 1) and r[3]<=maxPrice and r[4]<=maxDistance:
                valid.append(r)
        valid.sort(key=lambda r: (-r[1],-r[0]))
        return [r[0] for r in valid]
        