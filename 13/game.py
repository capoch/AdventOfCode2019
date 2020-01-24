from intcode import Receiver

class Game(Receiver):
  
  xCurr = 0
  yCurr = 0

  tileMap = dict()
  ballLocation = []
  paddleLocation = [0,0]
  blockCounter = 0
  direction = 0

  def __init__(self, name=None):
    self.inputCounter = 0
    self.inputMode = ("xPos", "yPos", "tileMode")
    self.name = name

  def processInput(self, output):
    inputSelector = self.inputCounter % 3
    if self.inputMode[inputSelector] == "xPos":
      #print("x: " + str(output))
      self.xCurr = output
      self.inputCounter += 1
    elif self.inputMode[inputSelector] == "yPos":
      self.yCurr = output
      #print("y: " + str(output))
      self.inputCounter += 1

    elif self.inputMode[inputSelector] == "tileMode":
      if self.xCurr == -1 and self.yCurr == 0:
        print("Current Score: " + str(output))
      if output == 3:
        self.paddleLocation = [self.xCurr, self.yCurr]
      elif output == 4:
        self.ballLocation = [self.xCurr,self.yCurr]

        if self.paddleLocation[0] < self.ballLocation[0]:
          self.direction = 1
        elif self.paddleLocation[0] > self.ballLocation[0]:
          self.direction = -1
        else:
          self.direction = 0
        
      self.inputCounter += 1
  def forwardData(self, data):
      self.processInput(data)
