class Clock_Angle:
    def __init__(self, hour, minutes):
        self.hour= hour
        self.minutes= minutes

    def calAngle(self):
        #hour angle position
        h = (self.hour * 360) / 12 + (self.minutes * 360) / (12 * 60)
        print(h)
        #minute angle position
        m = (self.minutes * 360) / (60)
        print(m)

        angle = abs(h - m)
        print(angle)
        if angle > 180:
            angle = 360 - angle

        return angle
        
