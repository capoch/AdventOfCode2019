def main():
  imageWidth = 25
  imageHeight = 6
  imageSize = imageWidth * imageHeight
  inputLocation = 'input.txt'

  with open(inputLocation, 'r') as input:
    completeData = input.read()
    layerCount = len(completeData) / (imageWidth * imageHeight)
    parsedImage = []
    for i in range(0,layerCount):
      imageLine = []
      dataSegment = completeData[i*imageSize:(i+1)*imageSize]
      for j in range(0, len(dataSegment)):
        imageLine.append(int(dataSegment[j:j+1]))
      parsedImage.append(imageLine)
  

  solutionString = intListToString(findNonTransparentPixels(transposeMatrix(parsedImage)))
  for i in range(0,6):
    print solutionString[i * 25:(i+1)*25]

def transposeMatrix(matrix):
  output = []
  for i in range(0, len(matrix[0])):
    column = []
    for j in range(0, len(matrix)):
      column.append(matrix[j][i])
    output.append(column)
  return output

def findNonTransparentPixels(matrix):
  result = []
  for i in range(0, len(matrix)):
    for j in range(0,len(matrix[i])):
      if matrix[i][j]==0:
        result.append(' ')
        break
      elif matrix[i][j]==1:
        result.append('#')
        break
      if j==len(matrix[i])-1:
        result.append(matrix[i][j])
  return result

def intListToString(theList):
  result = ""
  for i in range(0, len(theList)):
    result += str(theList[i])
  return result

main()
