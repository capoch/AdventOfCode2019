from intcode import Receiver

class Robot(Receiver):
  directions = ([0,1],[-1,0],[0,-1],[1,0])
  paintOrMove = 1
  shipMap = dict()
  positionList = list()

  def __init__(self, receiver=None, name=None):
    self.position = [0,0]
    self.direction = [0,1]
    self.receiver = receiver
    self.name = name

  def move(self):
    self.position[0] += self.direction[0]
    self.position[1] += self.direction[1]

  def turn(self, indicator):
    currentDirection = self.directions.index(self.direction)
    if indicator == 0:
      newDirection = (currentDirection + 1) % 4
    elif indicator == 1:
      newDirection = (currentDirection - 1) % 4
      if newDirection < 0:
        newDirection += 4
    else:
      print("Wrong direction indicator")
    self.direction = self.directions[newDirection]

  def forwardData(self, output):
      self.processInput(output)

  def processInput(self, data):
    if self.paintOrMove == 1:
      self.shipMap[tuple(self.position)] = data
      self.paintOrMove *= -1
    elif self.paintOrMove == -1:
      self.turn(data)
      self.positionList.append(self.position.copy())
      self.move()
      if tuple(self.position) in self.shipMap.keys():
        self.receiver.append(self.shipMap[tuple(self.position)])
      else:
        self.receiver.append(0)
      self.paintOrMove *= -1
