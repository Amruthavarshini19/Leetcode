class Solution(object):
    def carPooling(self, trips, capacity):
        change = [0]* 1001
        for num, start, end in trips:
            change[start]+=num
            change[end]-=num
        passengers = 0
        for location in range(1001):
            passengers+=change[location]
            if passengers>capacity:
                return False
        return True

        