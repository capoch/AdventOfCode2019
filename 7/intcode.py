class Intcode:

  relativeBase = 0
  codesProcessed = 0

  def __init__(self, memory):
    emptyMemory = [0 for d in range(0,100000000)]
    self.opcodes = memory
    self.opcodes.extend(emptyMemory)
    print("total length of memory: " + str(len(self.opcodes)))

  def mode(self, pointer, modeNumber, delta,debugMode):
    if modeNumber == 0:
      if(debugMode):
        print(str(pointer) + ": positional mode")
      return self.opcodes[self.opcodes[pointer+delta]]
    elif modeNumber == 1:
      if(debugMode):
        print(str(pointer) + ": absolute mode")
      return self.opcodes[pointer+delta]
    elif modeNumber ==2:
      if(debugMode):
        print(str(pointer) + ": relative mode with current base" + str(self.relativeBase))
      return self.opcodes[self.relativeBase + self.opcodes[pointer+delta]]
    else:
      print("invalid mode")

  def runProgram(self, input, debugMode):
    self.input = input
    pointer = 0
    output = None
    inputCounter = 0;

    while(True):
      if(debugMode):
        print("At pointer: " + str(pointer))
      instructionList = self.analyzeOpcode(self.opcodes[pointer], debugMode)
      if instructionList[0]!=99:
        leftValue = self.mode(pointer,instructionList[1],1,debugMode)
      if instructionList[0]==1 or instructionList[0]==2 or instructionList[0]==5 or instructionList[0]==6 or instructionList[0]==7 or instructionList[0]==8:
        rightValue = self.mode(pointer,instructionList[2],2, debugMode)
      if instructionList[0]==99:
        break
      elif instructionList[0]==1:
        self.opcodes[self.opcodes[pointer+3]]=leftValue + rightValue
        pointer += 4
      elif instructionList[0]==2:
        self.opcodes[self.opcodes[pointer+3]] = leftValue * rightValue
        pointer += 4
      elif instructionList[0]==3:
        print(leftValue)
        self.opcodes[leftValue]=input[inputCounter]
        if inputCounter == 0:
          self.state = input[inputCounter]
        inputCounter += 1
        pointer += 2
      elif instructionList[0]==4:
        output = leftValue
        print("Program Output: " +str(leftValue))
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
      elif instructionList[0]==9:
        self.relativeBase += leftValue
        pointer += 2
      else:
        print "Invalid Action Code(" + str(instructionList[0]) + ") you fucktard"
        print pointer
        break
    if(debugMode):
      print "final pointer: " + str(pointer)
    return output

  def analyzeOpcode(self,opcode, debugMode):
    self.codesProcessed += 1
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
    if(debugMode):
      print("actionCode " + str(actionCode)) 
    return [actionCode, indicatorOne, indicatorTwo]

