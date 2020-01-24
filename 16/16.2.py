def main():
    input = ''
    repeat = 10000
    inputlocation = 'input.txt'
    with open(inputlocation, 'r') as inputpart:
        inputstring = inputpart.read().strip()
        for i in range(0, repeat):
            input += inputstring
    messageOffset = int(input[0:7])
    workingData = [int(d) for d in input[messageOffset:]]
    workingData.reverse()
    counter = 0

# for digits in the 2nd half it's true that d(last -n) = sum of last n digits
    while counter < 100:
        for i in range(1, len(workingData)):            
                workingData[i] = (workingData[i] + workingData[i-1]) % 10
        counter += 1
    workingData.reverse()
    print(workingData[:8])

main()
