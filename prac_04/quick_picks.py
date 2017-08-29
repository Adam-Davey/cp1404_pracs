# import random
#
# numbers_in_line = 6
# minimum = 1
# maximum = 45
#
#
# def main():
#     quick_picks = int(input("how many quick picks?"))
#     while quick_picks < 0:
#         print("invalid")
#         quick_picks = int(input("how many quick picks?"))
#
#     for i in range(quick_picks):
#         for j in range(numbers_in_line):
#             number_picks = random.randint(minimum, maximum)
#             print("{:2}".format(number_picks), end=" ")
#
#
# main()

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
        quick_pick = []

        for lucky_num in range(num_per_line):
            winning_numbers = random.randint(minimum, maximum)
            while winning_numbers in quick_pick:
                winning_numbers = random.randint(minimum, maximum)
            quick_pick.append(winning_numbers)
        quick_pick.sort()

        print(" ".join("{:2}".format(winning_numbers) for winning_numbers in quick_pick))
            # print(winning_numbers)


main()
