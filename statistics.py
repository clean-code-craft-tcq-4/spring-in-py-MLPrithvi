def calculateStats(numbers):
  if isnan(numbers):
    return True
  elif isnumeric(numbers):
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
    
  
