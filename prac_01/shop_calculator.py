total_price = 0
number_of_items = int(input("number of items:"))
while number_of_items < 0:
    print("invalid number of items")
    number_of_items = int(input("number of items:"))

for price in range(number_of_items):
    price = float(input("price of item: $"))
    total_price += price

if total_price > 100:
    discount = total_price * 10 / 100
    total_price -= discount


print("total price for", number_of_items, "items is ", '${:.2f}'.format(total_price))
