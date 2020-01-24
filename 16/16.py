def main():
	input = "8087122458591454661908321864559580871224585914546619083218645595"	
	cycles = 100
	currentCycle = 0
	while currentCycle < cycles:
		input = executePhase(input)
		currentCycle += 1
	print(input)

def executePhase(input):
	output = ""
	inputList = [int(d) for d in str(input)]
	for i in range(0, len(inputList)):
		calculatedValueString = str(listProduct(calculatePattern(len(inputList),i+1), inputList))
		output += calculatedValueString[len(calculatedValueString)-1]
	return output

def listProduct(list1, list2):
	result = 0
	if len(list1) != len(list2):
		print("Fuck off")
	else:
		for i in range(0, len(list1)):
			result += list1[i]*list2[i]
	return result


def calculatePhaseOutput(input):
	inputList = [int(d) for d in str(input)]


def calculatePattern(length,n):
	basePattern = getNthBasePattern(n)
	resultingPattern = []
	while len(resultingPattern) + len(basePattern) <= length:
		resultingPattern.extend(basePattern)
	for i in range(0, len(basePattern)):
		if len(resultingPattern) == length + 1:
			break
		else:
			resultingPattern.append(basePattern[i])
	return resultingPattern[1:]


def getNthBasePattern(n):
	basePattern = []
	for i in range(0,n):
		basePattern.append(0)
	for i in range(0,n):
		basePattern.append(1)
	for i in range(0,n):
		basePattern.append(0)
	for i in range(0,n):
		basePattern.append(-1)
	return basePattern


main()
