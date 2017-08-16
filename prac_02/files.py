name_file = "name.txt"

# part 1
out_file = open("name.txt", "w")

name = str(input("what is your name:"))
print(name, file=out_file)  # file=out_file must save the name to name.txt
out_file.close()

# part 2
read_file = open(name_file, "r")  # r for read w for write
name = read_file.read().strip()  # strip removes line underneath?, read not readline
print("your name is", name)
read_file.close()

# part 3
numbers_file = open("numbers.txt", "r")
number1 = int(numbers_file.readline())  # remember to put int
number2 = int(numbers_file.readline())  # learn how to find lines**
print(number1 + number2)
