def format_data(data):
    # There are 9 columns in the first 8 rows
    # Each column means a different queue where first row means top and last row means bottom
    # Each column is separated by a tab
    # Store in a list of lists
    formatted_data = []

    for i in range(0, 8):
        temp_data = data[i].split(" ")
        finalJ = len(temp_data)
        counterSpaces = 0
        removeIndexes = []
        for j in range(0, finalJ):
            if temp_data[j] == "":
                counterSpaces += 1
                if counterSpaces == 4:
                    counterSpaces = 0
                    continue
                removeIndexes.append(j)
        for index in sorted(removeIndexes, reverse=True):
            del temp_data[index]
        formatted_data.append(temp_data)

    # Remove all the "[" and "]" from the list
    for i in range(0, 8):
        for j in range(0, 9):
            formatted_data[i][j] = formatted_data[i][j].replace("[", "")
            formatted_data[i][j] = formatted_data[i][j].replace("]", "")

    finalData = []
    for i in range(0, 9):
        finalData.append([])
        for j in range(0, 8):
            if formatted_data[j][i] != "":
                finalData[i].append(str(formatted_data[j][i]))
            # Take first element of finalData[i]
    return finalData


def formatMovements(data):
    movements = []
    for i in range(10, len(data)):
        # Split data[i] in 3 integers X, Y and Z
        # Where the data is "move X from Y to Z"
        # And save only the integers
        temp_data = data[i].split(" ")
        # Take only positions 1, 3 and 5
        temp_data = [temp_data[1], temp_data[3], temp_data[5]]
        movements.append(temp_data)
    return movements


def doMovements(queues, movement):
    # movement[0] = X
    # movement[1] = Y
    # movement[2] = Z
    # X = Position of the element to move
    # Y = Queue where the element is
    # Z = Queue where the element will be moved
    # Remove element from Y
    # Add element to Z
    for i in range(0, int(movement[0])):
        element = queues[int(movement[1]) - 1][0]
        queues[int(movement[1]) - 1].pop(0)
        queues[int(movement[2]) - 1].insert(0, element)


def doMovements2(queues, movement):
    temp = []
    for i in range(0, int(movement[0])):
        element = queues[int(movement[1]) - 1][0]
        queues[int(movement[1]) - 1].pop(0)
        temp.append(element)
    for i in range(0, int(movement[0])):
        queues[int(movement[2]) - 1].insert(0, temp[int(movement[0]) - 1 - i])


# Open day5/day5.txt file
with open("day5/day5.txt", "r") as f:
    # Read file
    data = f.read().splitlines()

print(data)

queues = format_data(data)
print(queues)

movements = formatMovements(data)
print(movements)

# Ask if it is part 1 or part 2
part = input("Part 1 or part 2? ")

if part == "1":
    for movement in movements:
        doMovements(queues, movement)
else:
    for movement in movements:
        doMovements2(queues, movement)

print(queues)
