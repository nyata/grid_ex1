# Detecting leap year
# year is inputted from command line
# 27.Oct.2015 Mana Sasagawa and Nagisa Yata

import sys

# define function which detect leapyear
# input : year (YYYY)
# output: boolean
def detect_leapyear(year):
  if int(year) % 4 == 0:
    if int(year) % 100 != 0 or \
       (int(year) % 100 == 0 and int(year) % 400 == 0): 
       return True 
  return False

# input a year from command line
argv = sys.argv
argc = len(argv)

# error
if argc < 2 or not argv[1].isdigit():
  print "You have to input year as argument"
  quit()

#output the result
if detect_leapyear(argv[1]):
  print argv[1] + " is a leap year"
else:
  print argv[1] + " is not a leap year"