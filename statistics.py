import math

def calculateStats(numbers):
#   if bool(numbers):
#     return math.nan
  if numbers != 0:
    l = len(numbers)
    avgVal = sum(numbers) / l
    maxVal = max(numbers)
    minVal = min(numbers)
  return avgVal,minVal,maxVal

def EmailAlert():
# def StatsAlerter(Threshold, Alert):
  

# def checkAndAlert(numbers):
  
