class Solution(object):
    def carFleet(self, target, position, speed):
        cars = sorted(zip(position,speed), reverse= True)
        s = []
        for pos , spd in cars:
            time = (target-pos)/float(spd)
            if not s or time>s[-1]:
                s.append(time)
        return len(s)
