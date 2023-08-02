def getScore(char):
    value = ord(char)
    if 65 <= value <= 90:
        return value - 38
    elif 97 <= value <= 122:
        return value - 96


def find_repeated(line):
    # Divide the line into 2 parts of equal length
    line = [line[: len(line) // 2], line[len(line) // 2 :]]
    # Compare both parts to search for the same character
    for i in range(len(line[0])):
        for j in range(len(line[1])):
            if line[0][i] == line[1][j]:
                return line[0][i]


def find3Repeated(lines):
    for c in lines[0]:
        if c in lines[1] and c in lines[2]:
            return c


# Read day3/day3.txt
with open("day3/day3.txt") as f:
    data = f.readlines()

totalScore = 0
found = False

print("Data without any process: ")
print(data)

for line in data:
    # Remove the newline character
    line = line[:-1]
    char = find_repeated(line)
    totalScore += getScore(char)

print("Total score: " + str(totalScore))

totalScore2 = 0

# Take the lines in groups of 3
for i in range(0, len(data), 3):
    # Remove the newline character
    data[i] = data[i][:-1]
    data[i + 1] = data[i + 1][:-1]
    data[i + 2] = data[i + 2][:-1]
    # Find the repeated character in each line
    char1 = find3Repeated([data[i], data[i + 1], data[i + 2]])
    totalScore2 += getScore(char1)

print("Total score 2: " + str(totalScore2))
