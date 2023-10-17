import datetime
class Zate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getWeekdayNumber(self):
        date_object = datetime.date(self.year, self.month, self.day)
        weekday_number = date_object.weekday()
        return weekday_number + 1

    def getWeekdayName(self):
        weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        return weekdays[self.getWeekdayNumber()]

    def getMonthName(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        return months[self.getMonth() - 1]


import datetime


class ZateExt(Zate):
    def addYears(self, years):
        new_date = datetime.date(self.year + years, self.month, self.day)
        return ZateExt(new_date.year, new_date.month, new_date.day)

    def subtractYears(self, years):
        new_date = datetime.date(self.year - years, self.month, self.day)
        return ZateExt(new_date.year, new_date.month, new_date.day)

    def addMonths(self, months):
        year_diff = (months + self.month - 1) // 12
        month = (self.month + months - 1) % 12 + 1
        year = self.year + year_diff
        new_date = datetime.date(year, month, self.day)
        return ZateExt(new_date.year, new_date.month, new_date.day)

    def subtractMonths(self, months):
        year_diff = (months + 11 - self.month) // 12
        month = (self.month - months + 11) % 12 + 1
        year = self.year - year_diff
        new_date = datetime.date(year, month, self.day)
        return ZateExt(new_date.year, new_date.month, new_date.day)

    def addDays(self, days):
        delta_days = datetime.timedelta(days=days)
        new_date = datetime.date(self.year, self.month, self.day) + delta_days
        return ZateExt(new_date.year, new_date.month, new_date.day)

    def subtractDays(self, days):
        delta_days = datetime.timedelta(days=days)
        new_date = datetime.date(self.year, self.month, self.day) - delta_days
        return ZateExt(new_date.year, new_date.month, new_date.day)
zate = Zate(2023, 10, 17)
print(zate.getYear())
print(zate.getMonth())
print(zate.getDay())
print(zate.getWeekdayNumber())
print(zate.getWeekdayName())
print(zate.getMonthName())