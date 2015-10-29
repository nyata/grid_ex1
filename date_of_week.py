# Determination of the day of the week
# 
# 28.Oct.2015 Nagisa Yata

from datetime import date
from leapyear import detect_leapyear


# define function
def determine_day_of_week(date):
  weekday_str = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  return weekday_str[date.weekday]

# start program
date = raw_input("Input the date (DD/MM/YYYY):")
split_date = date.split("/")

data_set = [2, 4, 6, 9, 11]

i = 0
year = 0
month = 0
day = 0
for s in split_date:
  if not s.isdigit():
    print "please input date"
    quit()
  elif i == 0:
    if len(s) > 2:
      print "please input date"
      quit()
    if int(s) < 1 or int(s) > 31:
      print "please input date"
      quit()
    else:
      day = int(s)
  elif i == 1:
    if len(s) > 2:
      print "please input date"
      quit()
    if int(s) < 1 or int(s) > 12:
      print "please input date"
      quit()
    if not s in data_list:
      if day > 30:
        print "please input date"
        quit()
    else:
      month = int(s)
  elif i == 2:
    if detect_leapyear(s):
      if month == 2:
        if day > 29:
          print "please input date"
          quit()
    else:
      if month == 2:
        if day > 28:
          print "please input date"
          quit()
    year = int(s)
  elif i > 2:
    print "please input date"
    quit()

if day == 0 or month == 0 or year == 0:
  print "please input date"
  quit()

# end validation

print datermine_day_of_week(datetime.date(year, month, day))
