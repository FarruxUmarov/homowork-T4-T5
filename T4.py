class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def getDay(self):
        if self.day >=1 and self.day <=10:
            print(f"sana: 0 {self.day}")
        elif self.day >= 10 and self.day <= 31:
            print(f"sana: {self.day}")
        else:
            print("Xatolik sana notogri kritildi!")
    
    def setDay(self, new_day):
        self.day = new_day
        if new_day >= 1 and new_day < 10:
            print(f"sana: 0{new_day}")
        elif new_day >= 10 and new_day <= 31:
            print(f"sana: {new_day}")
        else:
            print("Xatolik sana notogri kritildi!")
    
    def getMonth(self):
        if self.month >= 1 and self.month < 10:
            print(f"oy: 0{self.month}")
        elif self.month >= 10 and self.month <= 12:
            print(f"oy: {self.month}")
        else:
            print("Xatolik oy notogri kritildi!")
    
    def setMonth(self, new_month):
        self.month = new_month
        if new_month >= 1 and new_month < 10:
            print(f"oy: 0{new_month}")
        elif new_month >= 10 and new_month <= 12:
            print(f"oy: {new_month}")
        else:
            print("Xatolik oy notogri kritildi!")

    def getYear(self):
        if self.year >= 1900 and self.year <= 9999:
            print(f"yil: {self.year}")
        else:
            print("Xatolik yil notogri kritildi!")
            
    def setYear(self, new_year):
        self.year = new_year
        if new_year >= 1900 and new_year <= 9999:
            print(f"yil: {new_year}")
        else:
            print("Xatolik yil notogri kritildi!")

    def getDate(self):
        if self.day >= 1 and self.day < 10 and self.month >= 1 and self.month < 10 and self.year >= 1900 and self.year <= 9999:
            print(f"Hozirgi vaqt: 0{self.day}:0{self.month}:{self.year}")
        elif self.day >= 10 and self.day <= 31 and self.month >= 10 and self.month <= 12 and self.year >= 1900 and self.year <= 9999:
            print(f"Hozirgi vaqt: {self.day}:{self.month}:{self.year}")


    def setDate(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        if day >= 1 and day < 10 and month >= 1 and month < 10 and year >= 1900 and year <= 9999:
            print(f"Hozirgi vaqt: 0{day}/0{month}/{year}")
        elif day >= 10 and day <= 31 and month >= 10 and month <= 12 and year >= 1900 and year <= 9999:
            print(f"Hozirgi vaqt: {day}/{month}/{year}")

    def toString(self, new_day, new_month, new_year):
        if new_day >= 1 and new_day < 10 and new_month >= 1 and new_month < 10 and new_year >= 1900 and new_year <= 9999:
            print(f"Yangi vaqt strTypeda: 0{str(new_day)}:{str(new_month)}:{str(new_year)}")
        elif new_day >= 10 and new_day <= 31 and new_month >= 10 and new_month <= 12 and new_year >= 1900 and new_year <= 9999:
            print(f"Yangi vaqt strTypeda: {str(new_day)}:{str(new_month)}:{str(new_year)}")
    
    
day = int(input("Sana kiriting (1 dan - 31 gacha): "))
month = int(input("Oy kiriting (1 dan - 12 gacha): "))
year = int(input("Yil kiriting (1900 dan - 9999 gacha): "))

date = Date(day, month, year)

print("Xozirgi vaqt:")
date.getDay()
date.getMonth()
date.getYear()
date.getDate()

print("\nO`gargan vaqt")

day = int(input("Sana kiriting (1-31): "))
date.setDay(day)

month = int(input("Oy kiriting (1-12): "))
date.setMonth(month)

year = int(input("Yil kiriting (1900-9999): "))
date.setYear(year)

date.setDate(day, month, year)
date.toString(day, month, year)