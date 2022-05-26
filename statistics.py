def calculateStats(numbers):
  if numbers == 0:
    return nan
  l = len(numbers)
  avgVal = sum(numbers) / l
  maxVal = max(numbers)
  minVal = min(numbers)
  return avgVal,minVal,maxVal
