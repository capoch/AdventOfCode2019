class Intcode:
  
  _receiver = None

  def __init__(self, memory):
    self.opcodes = memory

  def setReceiver(self,receiver):
    self._receiver = receiver

  def runProgram(self, input):
    self.input = input
    pointer = 0
    output = None
    inputCounter = 0;
    while(True):
      instructionList = self.analyzeOpcode(self.opcodes[pointer])
      if instructionList[0]!=99:
        if instructionList[1]==1:
          leftValue = self.opcodes[pointer+1]
        else:
          leftValue = self.opcodes[self.opcodes[pointer+1]]
      if instructionList[0]==1 or instructionList[0]==2 or instructionList[0]==5 or instructionList[0]==6 or instructionList[0]==7 or instructionList[0]==8:
        if instructionList[2]==1:
          rightValue = self.opcodes[pointer+2]
        else:
          self.opcodes[pointer+2]
          rightValue = self.opcodes[self.opcodes[pointer+2]]
      if instructionList[0]==99:
        break
      elif instructionList[0]==1:
        self.opcodes[self.opcodes[pointer+3]]=leftValue + rightValue
        pointer += 4
      elif instructionList[0]==2:
        self.opcodes[self.opcodes[pointer+3]] = leftValue * rightValue
        pointer += 4
      elif instructionList[0]==3:
        self.opcodes[self.opcodes[pointer+1]]=input[inputCounter]
        if inputCounter == 0:
          self.state = input[inputCounter]
        inputCounter += 1
        pointer += 2
      elif instructionList[0]==4:
        output = leftValue
        #print leftValue
        pointer += 2
      elif instructionList[0]==5:
        if leftValue != 0:
          pointer = rightValue
        else:
          pointer += 3
      elif instructionList[0]==6:
        if leftValue == 0:
          pointer = rightValue
        else:
          pointer += 3
      elif instructionList[0]==7:
        if leftValue < rightValue:
          self.opcodes[self.opcodes[pointer+3]]=1
        else:
          self.opcodes[self.opcodes[pointer+3]]=0
        pointer += 4
      elif instructionList[0]==8:
        if leftValue == rightValue:
          self.opcodes[self.opcodes[pointer+3]]=1
        else:
          self.opcodes[self.opcodes[pointer+3]]=0
        pointer += 4
      else:
        print "Invalid Action Code(" + str(instructionList[0]) + ") you fucktard"
        print pointer
        break
    print "total pointer count: " + str(pointer)
    return output

  def callReceiver(receiver, input):
    receiver.runProgram(input)

  def analyzeOpcode(self,opcode):
    if len(str(opcode))==1:
      return [opcode,0,0]
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
    return [actionCode, indicatorOne, indicatorTwo]

