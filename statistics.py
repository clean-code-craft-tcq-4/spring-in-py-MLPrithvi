import math

def calculateStats(numbers):
  if numbers == 0:
    avgVal = math.nan
    minVal = math.nan
    maxVal = math.nan
  return avgVal,minVal,maxVal
#   if numbers != 0:
#     l = len(numbers)
#     avgVal = sum(numbers) / l
#     maxVal = max(numbers)
#     minVal = min(numbers)
