from planetarySystem import *
from math import gcd

def main():
  coordinateLists = ((-7,6,-12,4,0,0,0,0), (-1,-9,2,-17,0,0,0,0), (6,-9,-7,-12,0,0,0,0))
  cycleList = []
  for coordinateList in coordinateLists:
    cycleList.append(checkForCycles(coordinateList))

  print(cycleList)
  print(lcm_3(*cycleList))

def checkForCycles(list1):
  mem1 = set() 
  counter1 = 0

  while list1 not in mem1:
    mem1.add(list1)
    list1 = applyVelocities(calculateVelocities(list1))
    counter1 += 1
  mem1.add(list1)
  return (counter1)

def processList(theList):
   return applyVelocities(calculateVelocities(theList))

def calculateVelocities(theTuple):
    theList = list(theTuple)
    for i in range(0,4):
      for j in range(0,4):
        if i!=j and theList[j] > theList[i]:
          theList[i+4] += 1
        elif i!=j and theList[j] < theList[i]:
          theList[i+4] -= 1
    return theList.copy()

def applyVelocities(theList):
  for i in range(0,4):
    theList[i] += theList[i+4]
  return tuple(theList)

def lcm_2(a,b):
    return int((a * b) / gcd(a,b))

def lcm_3(a,b,c):
    return lcm_2(a, lcm_2(b,c))
main()
