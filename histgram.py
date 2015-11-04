# Determination of the Z boson mass
# 
# 4.Nov.2015 Mana Sasagawa and Nagisa Yata

import math
import os

#
# function of detect max value
#
def get_max(data):
  i = 0
  max = 0
  for d in data:
    if i == 0:
      max = float(d)
    else:
      if max < float(d):
        max = float(d)
    i += 1
  
  return max

#
# function of showing histgram
#
def show_histgram(data):
  # count point and get maximum y value
  x_max = get_max(data)
  x_max = int(math.floor(x_max))
  print "maximum of x range :" + str(x_max)

  x = [0] * (x_max + 1)
  y_max = 0
  y_max_index = 0
  for d in data:
    x[int(math.floor(float(d)))] += 1
    # check maximum y value
    if y_max < x[int(math.floor(float(d)))]:
      y_max = x[int(math.floor(float(d)))]
      y_max_index = int(math.floor(float(d)))

  # show and output histgram
  i = 0
  file = open("output_histgram.txt", "w")
  for d in x:
    row = str(i) + " "
    for num in range(0, d):
      row += "*"
    #print row
    file.write(row + "\n")
    i += 1
  file.close()

  # FWHM
  # search ymax/2 value
  half_ymax = y_max / 2

  # search nearest value to half ymax value
  # plus direction
  x2 = -1
  min = 0
  for idx in range(y_max_index, x_max):
    if x2 < 0:
      x2 = idx
      min = abs(half_ymax - x[idx])
    elif min > abs(half_ymax - x[idx]):
      x2 = idx
      min = abs(half_ymax - x[idx])

  # minus direction
  x1 = -1
  min = 0
  for idx in range(0, y_max_index-1):
    if x1 < 0:
      x1 = idx
      min = abs(half_ymax - x[idx])
    elif min > abs(half_ymax - x[idx]):
      x1 = idx
      min = abs(half_ymax - x[idx])


  if x1 < 0 or x2 < 0:
    print "cannot determine the FWHM"
  else:
    print "y_max: " + str(y_max)
    print "y_max index: " + str(y_max_index)
    print "half of y_max value index: " + str(x2) + ", " + str(x1)
    print "FWHM: " + str(x2 - x1)


# start program

# get binary file
filename = "masses.txt"
url = "http://www.atlas.uni-wuppertal.de/~harenber/masses.txt"
os.system("wget " + url)

# read file
file = open(filename)
bozon_data = file.readlines()
file.close()

show_histgram(bozon_data)
