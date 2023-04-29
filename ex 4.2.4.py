import datetime
import calendar

date_input = input("Enter a date (dd/mm/yyyy): ")
day, month, year = map(int, date_input.split('/'))
weekday_num = datetime.date(year, month, day).weekday()     # get number of the day in the week
weekday_name = calendar.day_name[weekday_num]   # get the name of the day

print(weekday_name)
