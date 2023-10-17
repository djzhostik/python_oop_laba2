import datetime
class Month:
    def __init__(self, month_number):
        self.month_number = month_number

    def getMonthNumber(self):
        return self.month_number

    def getMonthName(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December']
        return months[self.getMonthNumber() - 1]

    def getLastDayNumber(self):
        if self.month_number == 12:
            next_month = 1
            next_year = datetime.date.today().year + 1
        else:
            next_month = self.month_number + 1
            next_year = datetime.date.today().year

        last_day = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)

        return last_day.day

    def getFirstWeekdayNumber(self):
        first_day = datetime.date(datetime.date.today().year, self.month_number, 1)
        return first_day.weekday()

    def getLastWeekdayNumber(self):
        last_day = datetime.date(datetime.date.today().year, self.month_number, self.getLastDayNumber())
        return last_day.weekday()
month = Month(9)
print(month.getMonthNumber())
print(month.getMonthName())
print(month.getLastDayNumber())
print(month.getFirstWeekdayNumber())
print(month.getLastWeekdayNumber())