from datetime import datetime

class Period:
  def __init__(self, start_time, end_time):
    self.start_time = start_time
    self.end_time = end_time

  def get_seconds_diff(self):
    diff = self.end_time - self.start_time
    return diff.total_seconds()

  def get_minutes_diff(self):
    seconds_diff = self.get_seconds_diff()
    minutes_diff = seconds_diff / 60
    return minutes_diff

  def get_hours_diff(self):
    minutes_diff = self.get_minutes_diff()
    hours_diff = minutes_diff / 60
    return hours_diff

  def get_days_diff(self):
    hours_diff = self.get_hours_diff()
    days_diff = hours_diff / 24
    return days_diff

start_time = datetime(2022, 1, 1, 0, 0, 0)
end_time = datetime(2022, 1, 2, 12, 0, 0)

period = Period(start_time, end_time)

seconds_diff = period.get_seconds_diff()
print(seconds_diff)

minutes_diff = period.get_minutes_diff()
print(minutes_diff)

hours_diff = period.get_hours_diff()
print(hours_diff)

days_diff = period.get_days_diff()
print(days_diff)