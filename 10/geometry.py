import math

class Point(tuple):
  def __new__(self, x, y):
    return tuple.__new__(Point,(x,y))

  def __str__(self):
    return "Point(" + str(self[0]) + ", " + str(self[1]) + ")"

  #def __getitem__(self, x):
  #  if x==0 or x==1:
  #    return self[x]
  #  else:
  #    print("Point is two-dimensionally implemeted")

  def distanceFrom(self, pointX):
    return math.sqrt(math.pow(pointX.y - self[1], 2) + math.pow(pointX.x - self[0], 2))

  def convertToPolar(self):
    return Point(math.sqrt(math.pow(self[0],2)+math.pow(self[1],2)),math.atan2(self[0], self[1]))

  def convertToCartesian(self):
    return Point(self[0] * math.sin(self[1]), self[0] * math.cos(self[1]))

  def changeCenterOfCoordinates(self, centerX, centerY):
    return Point(self[0]-centerX, self[1]-centerY)

  def flipYAxis(self):
    return Point(self[0], - self[1])

class Vector:
  def __init__(self,point):
    self.x = point[0]
    self.y = point[1]

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def product(self,vector):
    return self.x * vector.x + self.y * vector.y

  def abs(self):
    return math.sqrt(math.pow(self.x,2)+math.pow(self.y,2))

  def direction(self, vector):
    return self.product(vector) / (self.abs() * vector.abs())


class Map:
  asteroids = set()
  def __init__(self, inputLocation):
    with open(inputLocation, 'r') as input:
      lineCount = 0
      line = input.readline()
      while line:
        for i in range(0, len(line)):
          if line[i]=='#':
            self.asteroids.add(Point(i, lineCount))
        line = input.readline()
        lineCount += 1

  def getAsteroids(self):
    return self.asteroids
