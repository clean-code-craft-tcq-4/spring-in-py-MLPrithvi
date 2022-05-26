from statistics import mean
import statistics

def calculateStats(numbers):
  avgVal = mean(numbers)
  maxVal = max(numbers)
  minVal = min(numbers)
  return avgVal,minVal,maxVal
