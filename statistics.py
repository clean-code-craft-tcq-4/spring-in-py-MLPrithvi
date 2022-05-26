def calculateStats(numbers):
  l = len(numbers)
  avgVal = sum(numbers) / l
  maxVal = max(numbers)
  minVal = min(numbers)
  return avgVal,minVal,maxVal

def CheckNumeric(numbers):
  l = len(numbers)
  for i in range(l):
    value = isinstance(i, str)
    return value

# def EmailAlert():
#   i = 0
#   i += 1
#   return i

# def LEDAlert():
#   return 3

# def StatsAlerter(Thres, Alert):
#   def checkAndAlert(numbers):
    
  
