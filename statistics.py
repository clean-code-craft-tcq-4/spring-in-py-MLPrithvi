from statistics import *
import statistics

def calculateStats(numbers):
  avgVal = statistics.mean(numbers)
  maxVal = max(numbers)
  minVal = min(numbers)
  return avgVal, minVal, maxVal
