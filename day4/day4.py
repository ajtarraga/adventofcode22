def separateNumbers(line):
    # Convert all the lines like "1-3" into [1, 2, 3], "2-5" into [2, 3, 4, 5], etc.
    # The line is a list of strings like ["1-3", "2-5"]
    # The line is converted into a list of lists of integers like [[1, 2, 3], [2, 3, 4, 5]]
    for i in range(len(line)):
        line[i] = line[i].split("-")
        for j in range(len(line[i])):
            line[i][j] = int(line[i][j])
        line[i] = list(range(line[i][0], line[i][1] + 1))
    return line


def searchContains(line):
    # Search if line[0] contains all the numbers in line[1] or vice versa
    # line[0] and line[1] are lists of integers
    # Return True if line[0] contains all the numbers in line[1] or vice versa
    # Return False otherwise
    if len(line[0]) >= len(line[1]):
        for i in range(len(line[1])):
            if line[1][i] not in line[0]:
                return False
        return True
    else:
        for i in range(len(line[0])):
            if line[0][i] not in line[1]:
                return False
        return True


def overlaps(line):
    # Search if line[0] and line[1] have any overlapping numbers
    # line[0] and line[1] are lists of integers
    # Return True if line[0] and line[1] have any overlapping numbers
    # Return False otherwise
    for i in range(len(line[0])):
        if line[0][i] in line[1]:
            return True
    return False


# Read day4/day4.txt
with open("day4/day4.txt") as f:
    data = f.readlines()

print(data)

counter = 0
counterOverlaps = 0

for line in data:
    line = line.split()
    # Separate line[0] into 2 parts divided by the comma
    line = line[0].split(",")
    separateNumbers(line)
    if searchContains(line):
        print(line)
        counter += 1
    if overlaps(line):
        print(line)
        counterOverlaps += 1

print("Total number of containable bags: " + str(counter))

print("Total number of overlapping bags: " + str(counterOverlaps))
