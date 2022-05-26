def calculateStats(numbers):
  if type(numbers) == str:
    return True
  elif type(numbers) == float:
    l = len(numbers)
    avgVal = sum(numbers) / l
    maxVal = max(numbers)
    minVal = min(numbers)
    return avgVal,minVal,maxVal

# def EmailAlert():
#   i = 0
#   i += 1
#   return i

# def LEDAlert():
#   return 3

# def StatsAlerter(Thres, Alert):
#   def checkAndAlert(numbers):
    
  
