# Read day2.txt
with open("day2/day2.txt") as f:
    data = f.readlines()

totalScore = 0
totalScore2 = 0

print("Data without any process: ")
print(data)

for line in data:
    # Split the line into a list of strings
    line = line.split()
    if line[0] == "A":
        if line[1] == "Y":
            totalScore += 6
        elif line[1] == "X":
            totalScore += 3
    if line[0] == "B":
        if line[1] == "Z":
            totalScore += 6
        elif line[1] == "Y":
            totalScore += 3
    if line[0] == "C":
        if line[1] == "X":
            totalScore += 6
        elif line[1] == "Z":
            totalScore += 3
    if line[1] == "X":
        totalScore += 1
        if line[0] == "A":
            totalScore2 += 3
        elif line[0] == "B":
            totalScore2 += 1
        elif line[0] == "C":
            totalScore2 += 2
    elif line[1] == "Y":
        totalScore2 += 3
        totalScore += 2
        if line[0] == "A":
            totalScore2 += 1
        elif line[0] == "B":
            totalScore2 += 2
        elif line[0] == "C":
            totalScore2 += 3
    elif line[1] == "Z":
        totalScore2 += 6
        totalScore += 3
        if line[0] == "A":
            totalScore2 += 2
        elif line[0] == "B":
            totalScore2 += 3
        elif line[0] == "C":
            totalScore2 += 1

print("Total score: " + str(totalScore))

print("Total score 2: " + str(totalScore2))
