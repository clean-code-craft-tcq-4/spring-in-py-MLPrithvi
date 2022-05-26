def calculateStats(numbers):
  l = len(numbers)
  avgVal = sum(numbers) / l
  maxVal = max(numbers)
  minVal = min(numbers)
  return avgVal,minVal,maxVal
