class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        degreesPerMin = 6
        degreesPerHour = 30

        MinuteAngle = minutes*degreesPerMin
        HourAngle = hour * degreesPerHour

        finalAngle = abs(HourAngle - MinuteAngle)
        

        change = minutes/2
        if change > 0:

            finalAngle -= change
        if finalAngle > 180:
            finalAngle = 360 - finalAngle
            return float(abs(finalAngle))
        else:
            return float(abs(finalAngle))

print(Solution().angleClock(3,15))