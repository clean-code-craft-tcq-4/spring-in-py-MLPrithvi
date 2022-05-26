from statistics import *

def calculateStats(numbers):
  avgVal = statistics.mean(numbers)
  maxVal = max(numbers)
  minVal = min(numbers)
  return avgVal, minVal, maxVal
