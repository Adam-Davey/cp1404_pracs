import random

num_per_line = 6

minimum = 1
maximum = 45

def main():
    quick_picks = int(input("how many quick picks would you like?:"))
    while quick_picks < 0:
        print("please enter a number")
        quick_picks = int(input("how many quick picks would you like?:"))

    for i in range(quick_picks):
        for lucky_num in range(num_per_line):
            winning_numbers = random.randint(minimum, maximum)
            print("{:2}".format(winning_numbers), end=" ")
            # print(winning_numbers)

main()
