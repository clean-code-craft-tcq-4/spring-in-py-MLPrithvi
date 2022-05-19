from statistics import mean
def calculateStats(numbers):
  avg = statistics.mean(numbers)
  max = max(numbers)
  min = min(numbers)
  return avgVal, minVal, maxVal
