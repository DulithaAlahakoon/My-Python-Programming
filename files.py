fileh = open("text.txt")

for line in fileh:
  if line.startswith("From:"):
    print(line.rstrip())