# Determination of the day of the week
# 
# 28.Oct.2015 Nagisa Yata

import datetime
import math

# define function
def determine_day_of_week(date_original):
  weekday_str = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

  year = date_original.year
  month = date_original.month
  
  # January and Feburary are operated 
  # as 13 and 14 in previous year
  if month < 3:
    month += 12
    year -= 1

  date = datetime.date(year, month, date_original.day)

  capital_y = date.year
  
  # Gregorian calendar
  gamma = 6 * math.floor(capital_y/100) + math.floor(capital_y / 400)
  
  # Julian calendar
  if date.year < 1582 and date.year > 4:
    gamma = 5

  # Zeller's congruence
  # this congruence represent Saturday is 0
  # then "-2" is used for number moved for index
  weekday = (date.day + math.floor(26 * (date.month + 1) / 10) + capital_y \
            + math.floor(capital_y / 4) + gamma) % 7 - 2
  
  return weekday_str[int(weekday)]
    

# start program
date = raw_input("Input the date (DD/MM/YYYY):")
split_date = date.split("/")

data_set = [2, 4, 6, 9, 11]

i = 0
y = 0
m = 0
d = 0
for s in split_date:
  if not s.isdigit():
    print "1please input date"
    quit()
  elif i == 0:
    d = int(s)
  elif i == 1:
    m = int(s)
  elif i == 2:
    y = int(s)
  elif i > 2:
    print "please input date"
    quit()
  i += 1

if d == 0 or m == 0 or y == 0:
  print "2please input date"
  quit()

# end validation

print determine_day_of_week(datetime.date(y,m,d))
