def calculateStats(numbers):
  if numbers == 0:
    avgVal = 'nan'
    minVal = 'nan'
    maxVal = 'nan'
  if numbers != 0:
    l = len(numbers)
    avgVal = sum(numbers) / l
    maxVal = max(numbers)
    minVal = min(numbers)
  return avgVal,minVal,maxVal
