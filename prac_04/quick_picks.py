import random

numbers_in_line = 6
minimum = 1
maximum = 45


def main():
    quick_picks = int(input("how many quick picks?"))
    while quick_picks < 0:
        print("invalid")
        quick_picks = int(input("how many quick picks?"))

    for i in range(quick_picks):
        for j in range(numbers_in_line):
            number_picks = random.randint(minimum, maximum)
            print("{:2}".format(number_picks), end=" ")


main()

# import random
#
# num_per_line = 6
#
# minimum = 1
# maximum = 45
#
#
# def main():
#     quick_picks = int(input("how many quick picks would you like?:"))
#     while quick_picks < 0:
#         print("please enter a number")
#         quick_picks = int(input("how many quick picks would you like?:"))
#
#     for i in range(quick_picks):
#         for lucky_num in range(num_per_line):
#             winning_numbers = random.randint(minimum, maximum)
#             print("{:2}".format(winning_numbers), end=" ")
#             # print(winning_numbers)
#
#
# main()
