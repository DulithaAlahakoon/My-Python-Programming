fileh = open("text2.txt", "w")

name = input("Enter your name: ")
age = int(input("Enter your age: ")) 
fileh.write("Name: " + name + "\n")
fileh.write("Age: " + str(age))

fileh.close()

fileh = open("text2.txt", "r")
print(fileh.read())
