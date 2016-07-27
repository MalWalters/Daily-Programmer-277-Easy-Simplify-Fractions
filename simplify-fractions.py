numbers = open('numbers.txt').read().split()

def find_lowest(num, denom):
    remainder = 1
    while remainder > 0:
        remainder = num % denom
        num = denom
        denom = remainder
    return num

for x in range (0, len(numbers),2):
    lowest = find_lowest(int(numbers[x]), int(numbers[x+1]))
    print(numbers[x] + "/" + numbers[x+1] + " simplifies to: " + str(int(numbers[x]) / lowest) + "/" + str(int(numbers[x+1])/lowest))
