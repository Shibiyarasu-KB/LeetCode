class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        person = 1
        direction = 1 # +1 if it is front , -1 if it is backward

        for i in range(time): #iteration times
            if person == n:
                direction = -1
            elif person == 1:
                direction = 1
            person+=direction
        return person