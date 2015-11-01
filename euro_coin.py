# Count number of coins
# how many needed to pay the input amount
# 27.Oct.2015 Mana Sasagawa and Nagisa Yata

import math

#Get the input number formed ##.$$
#amout = ##.$$
amount = input("Enter a Euro amount:")
#coin = [## , $$]
coin = str(amount).split(".")

euro_list = [2, 1]
cent_list = [50, 20, 10, 5, 2, 1]

i = 0
coin_num = 0
#value is the array for the result
value = [0] * 8
left = 0


for c in coin:
  if not c.isdigit():
    print "error: please input as digit"
    quit()
  else:
    left = int(c)
    #calculate ##
    if i == 0:
      j = 0
      for e in euro_list:
        #value is the number of the each euro coin
        value[j] = math.floor(left / e)
        #left is the rest of the euro amount
        left = left % e
        #calculate the total number of the coins
        coin_num += value[j]
        j += 1
    #calculate $$
    elif i == 1:
      for e in cent_list:
        value[j] = math.floor(left / e)
        left = left % e
        coin_num += value[j]
        j += 1
    else:
      print "error: please input as digit"
      quit()
  i += 1

print "you need at least " + str(int(coin_num)) + " coins"
print "2 EUR: ", int(value[0])
print "1 EUR: ", int(value[1])
print "50 ct: ", int(value[2])
print "20 ct: ", int(value[3])
print "10 ct: ", int(value[4])
print "5  ct: ", int(value[5])
print "2  ct: ", int(value[6])
print "1  ct: ", int(value[7])