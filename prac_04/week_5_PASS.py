# nice_things = (input("nice stuff"))
# nice_count = 0
# xmas_list = []
# for i in range(nice_things):
#     nice_count += 1
#     if nice_things > 10:
#         xmas_list = [input("what would you like for xmas?:")]
#     elif nice_things == 0:
#         print("sad message")
#     print(xmas_list)
#
#
# wishlist = []
#
# number = 10
# while number != 0:
#     number = int(input('How many nice things have you said today?'))
#     if number > 10:
#         wishlist.append(input('What do you want?'))
# print("sad message")
#
# print(wishlist)



score = int(input("what do you rate the item?:"))
try:
    while score < 10 and score >0:
        print("thanks")
except:
    while score > 10: #and < 0:
        print("try again plese")
