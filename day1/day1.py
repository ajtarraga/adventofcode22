#!/usr/bin/python3

# Read file "input.txt"
with open("day1/input.txt", "r") as f:
    # Read all lines
    lines = f.readlines()

# Remove newline characters
lines = [line.strip() for line in lines]

max = 0
max_local = 0
elf_maximum = 0
elf_local = 1

list_top3 = []

for line in lines:
    if line == "":
        elf_local += 1
        list_top3.append(max_local)
        max_local = 0
        continue
    max_local = max_local + int(line)
    if max_local > max:
        max = max_local
        elf_maximum = elf_local

print("The maximum number of Calories is " + str(max) + ".")
print("The elf that should eat the cookie is " + str(elf_maximum) + ".")

list_top3.sort(reverse=True)

print(
    "The top 3 elves are: "
    + str(list_top3[0])
    + ", "
    + str(list_top3[1])
    + ", "
    + str(list_top3[2])
    + "."
)

print(
    "The addition of the top 3 elves is "
    + str(list_top3[0] + list_top3[1] + list_top3[2]) 
    + "."
)
