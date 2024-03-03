class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def setTime(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def sozlashTime(self):
        if self.second >= 60:
            self.minute += self.second // 60
            self.second %= 60
        if self.minute >= 60:
            self.hour += self.minute // 60
            self.minute %= 60
        if self.hour >= 24:
            self.hour %= 24

    def yangiSecond(self):
        self.second += 1
        self.sozlashTime()

    def oldingiSecond(self):
        self.second -= 1
        if self.second < 0:
            self.second = 59
            self.minute -= 1
            if self.minute < 0:
                self.minute = 59
                self.hour -= 1
                if self.hour < 0:
                    self.hour = 23

    def getTime(self):
        print(f"Time: {self.hour:02d}:{self.minute:02d}:{self.second:02d}")

hour = int(input("Soat kiriting (0 dan - 23 gacha): "))
minute = int(input("Daqiqa kiriting (0 dan - 59 gacha): "))
second = int(input("Sekund kiriting (0 dan - 59 gacha): "))

time = Time(hour, minute, second)

print("\nOld time:")
time.getTime()

newHour = int(input("\nYangi soat kiriting (0 dan - 23 gacha): "))
newMinute = int(input("Yangi daqiqa kiriting (0 dan - 59 gacha): "))
newSecond = int(input("Yangi sekund kiriting (0 dan - 59 gacha): "))

time.setTime(newHour, newMinute, newSecond)

print("\nNew Time:")
time.getTime()

print("\nNext second:")
time.yangiSecond()
time.getTime()

print("\nPrevious second:")
time.oldingiSecond()
time.getTime()