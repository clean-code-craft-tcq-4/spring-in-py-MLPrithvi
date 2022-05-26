import math as m

def calculateStats(numbers):
  l = len(numbers)
  avgVal = sum(numbers) / l
  maxVal = max(numbers)
  minVal = min(numbers)
  return avgVal,minVal,maxVal

def checkNumeric(numbers):
  l = len(numbers)
  for i in range(l):
    value = m.isnan(i)
    return value

# def EmailAlert():
#   i = 0
#   i += 1
#   return i

# def LEDAlert():
#   return 3

# def StatsAlerter(Thres, Alert):
#   def checkAndAlert(numbers):
    
  
