from planetarySystem import *

def main():
  list1 = [-7,6,-12,4,0,0,0,0]  
  list2 = [-1,-9,2,-17,0,0,0,0] 
  list3 = [6,-9,-7,-12,0,0,0,0]  

  checkForCycles(list1)
  checkForCycles(list2)
  checkForCycles(list3)  

def checkForCycles(list1):
  mem1 = []
  counter1 = 0

  while list1 not in mem1:
    mem1.append(list1.copy())
    list1 = processList(list1)
    counter1 += 1
  mem1.append(list1)
  print(counter1)

def processList(theList):
  tempList = calculateVelocities(theList)
  return applyVelocities(tempList)

def calculateVelocities(theList):
    for i in range(0,4):
      for j in range(0,4):
        if i!=j and theList[j] > theList[i]:
          theList[i+4] += 1
        elif i!=j and theList[j] < theList[i]:
          theList[i+4] -= 1
    print(theList)
    return theList.copy()

def applyVelocities(theList):
  for i in range(0,4):
    theList[i] += theList[i+4]
    theList[i+4] = 0
  print(theList)
  return theList.copy()
main()
