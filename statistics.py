import math as m

def calculateStats(numbers):
  if isinstance(numbers, str):
    l = len(numbers)
    for i in range(l):
      value = m.isnan(i)
      return value
  if not isinstance(numbers, str):
    l = len(numbers)
    if l != 0:
      avgVal = sum(numbers) / l
      maxVal = max(numbers)
      minVal = min(numbers)
      return avgVal,minVal,maxVal

# def EmailAlert(e):
#   i = 0
#   if 
#   i += 1
#   return i

# def LEDAlert(j):
  

# def StatsAlerter(Thres, Alert):
#   def checkAndAlert(numbers):
#     if numbers > Thres:
      
    
  
