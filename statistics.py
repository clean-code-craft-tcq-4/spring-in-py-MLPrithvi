import math

def calculateStats(numbers):
  if numbers == 0:
    avgVal = NAN
    minVal = NAN
    maxVal = NAN
  else:
    l = len(numbers)
    avgVal = sum(numbers) / l
    maxVal = max(numbers)
    minVal = min(numbers)
  return avgVal,minVal,maxVal
