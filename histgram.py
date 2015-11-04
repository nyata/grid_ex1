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
  # count point
  x_max = int(math.floor(get_max(data)))
  x = [0] * (x_max + 1)
  for d in data:
    x[int(math.floor(float(d)))] += 1

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
