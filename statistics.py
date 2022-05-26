import math as m

def calculateStats(numbers):
  if type(numbers) == list:
    l = len(numbers)
    for i in range(l):
      if type(numbers[i]) == str:
        value = m.isnan(i)
        return value
      elif (type(numbers[i]) == float) or (type(numbers[i]) == int) and (l != 0):
        avgVal = sum(numbers) / l
        maxVal = max(numbers)
        minVal = min(numbers)
        return avgVal,minVal,maxVal

# def EmailAlert(e):
#   i = 0
#   if 
#   i += 1
#   return i

# def LEDAlert(j):
  

# def StatsAlerter(Thres, Alert):
#   def checkAndAlert(numbers):
#     if numbers > Thres:
      
    
  
