def main():
  imageWidth = 25
  imageHeight = 6
  imageSize = imageWidth * imageHeight
  inputLocation = 'input.txt'

  with open(inputLocation, 'r') as input:
    completeData = input.read()
    layerCount = len(completeData) / (imageWidth * imageHeight)
    print layerCount
    parsedImage = []
    for i in range(0,layerCount):
      imageLine = []
      dataSegment = completeData[i*imageSize:(i+1)*imageSize]
      for j in range(0, len(dataSegment)):
        imageLine.append(int(dataSegment[j:j+1]))
      parsedImage.append(imageLine)
  
  minZeroLayer = minFunctionAppliedToList(countZerosInList, parsedImage)

  print minZeroLayer

  print countNumberInList(minZeroLayer,1) * countNumberInList(minZeroLayer,2)


def countZerosInList(theList):
  return countNumberInList(theList, 0)

def countNumberInList(theList, theNumber):
  counter = 0
  for element in theList:
    if element == theNumber:
      counter += 1
  return counter

def minFunctionAppliedToList(theFunction, theList):
  minValue = theFunction(theList[0])
  targetElement = None
  for element in theList:
    if theFunction(element) < minValue:
      minValue = theFunction(element)
      targetElement = element
  return targetElement










main()
