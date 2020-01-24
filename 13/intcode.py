class Receiver:
  def __init__(self, name):
      self.name = name

  def forwardData(self,output):
    return output

class Intcode:
  receivers = []
  positionList = list()
  relativeBase = 0
  codesProcessed = 0


  def __init__(self, memory, sender, receivers):
    emptyMemory = [0 for d in range(0,1000000)]
    self.opcodes = memory
    self.opcodes.extend(emptyMemory)
    self.sender = sender
    self.receivers = receivers
    print("total length of memory: " + str(len(self.opcodes)))

  def mode(self, pointer, modeNumber, delta,debugMode):
    if modeNumber == 0:
      if(debugMode):
        print(str(pointer) + ": positional mode")
      return self.opcodes[pointer+delta]
    elif modeNumber == 1:
      if(debugMode):
        print(str(pointer) + ": absolute mode")
      return pointer+delta
    elif modeNumber ==2:
      if(debugMode):
        print(str(pointer) + ": relative mode with current base" + str(self.relativeBase))
      return self.relativeBase + self.opcodes[pointer+delta]
    else:
      print("invalid mode")

  def runProgram(self, debugMode):
    pointer = 0
    output = None
    inputCounter = 0;

    while(True):# and self.codesProcessed < 90):
      if(debugMode):
        print("At pointer: " + str(pointer))
      instructionList = self.analyzeOpcode(self.opcodes[pointer], debugMode)
      if instructionList[0]!=99:
        leftValue = self.mode(pointer,instructionList[1],1,debugMode)
      if instructionList[0]==1 or instructionList[0]==2 or instructionList[0]==5 or instructionList[0]==6 or instructionList[0]==7 or instructionList[0]==8:
        rightValue = self.mode(pointer,instructionList[2],2, debugMode)
      if instructionList[0]==1 or instructionList[0]==2 or instructionList[0]==7 or instructionList[0]==8:
        targetValue = self.mode(pointer, instructionList[3],3, debugMode)
      if instructionList[0]==99:
        break
      elif instructionList[0]==1:
        self.opcodes[targetValue]=self.opcodes[leftValue] + self.opcodes[rightValue]
        pointer += 4
      elif instructionList[0]==2:
        self.opcodes[targetValue] = self.opcodes[leftValue] * self.opcodes[rightValue]
        pointer += 4
      elif instructionList[0]==3:
        self.opcodes[leftValue]=self.receivers[0].direction
        pointer += 2
      elif instructionList[0]==4:
        output = self.opcodes[leftValue]
        self.sendToReceivers(output, debugMode)
        if(debugMode):  
          print("Program Output: " +str(self.opcodes[leftValue]))
        pointer += 2
      elif instructionList[0]==5:
        if self.opcodes[leftValue] != 0:
          pointer = self.opcodes[rightValue]
        else:
          pointer += 3
      elif instructionList[0]==6:
        if self.opcodes[leftValue] == 0:
          pointer = self.opcodes[rightValue]
        else:
          pointer += 3
      elif instructionList[0]==7:
        if self.opcodes[leftValue] < self.opcodes[rightValue]:
          self.opcodes[targetValue]=1
        else:
          self.opcodes[targetValue]=0
        pointer += 4
      elif instructionList[0]==8:
        if self.opcodes[leftValue] == self.opcodes[rightValue]:
          self.opcodes[targetValue]=1
        else:
          self.opcodes[targetValue]=0
        pointer += 4
      elif instructionList[0]==9:
        self.relativeBase += self.opcodes[leftValue]
        pointer += 2
      else:
        print("Invalid Action Code(" + str(instructionList[0]) + ") you fucktard")
        print(pointer)
        break
    if(debugMode):
      print("final pointer: " + str(pointer))
    #return self.receivers[0].tileMap
    return self.receivers[0].blockCounter

  def analyzeOpcode(self,opcode, debugMode):
    self.codesProcessed += 1
    if len(str(opcode))==1:
      return [opcode,0,0,0]
    else:
      actionCode = int(str(opcode)[-2:])
    if len(str(opcode)) >= 3:
      indicatorOne = int(str(opcode)[-3:-2])
    else:
      indicatorOne = 0
    if len(str(opcode)) >= 4:
      indicatorTwo = int(str(opcode)[-4:-3])
    else:
      indicatorTwo = 0
    if len(str(opcode)) >= 5:
      indicatorThree = int(str(opcode)[-5:-4])
    else:
      indicatorThree = 0
    if(debugMode):
      print("actionCode " + str(actionCode)) 
    return [actionCode, indicatorOne, indicatorTwo, indicatorThree]

  def sendToReceivers(self, output, debugMode=False):
    for receiver in self.receivers:
      if(debugMode):
        print("Receiver " + receiver.name + " called")
      receiver.forwardData(output)
