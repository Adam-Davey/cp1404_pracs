import random

max_increase = 0.175
max_decrease = 0.05
min_price = 0.01
max_price = 100

initial_price = 10.00
output_file = "file.txt"

price = initial_price
day = 0

print("starting price:", "${:.2f}".format(price))

out_file = open(output_file, "w")

while min_price <= price <= max_price:
    price_change = 0

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, max_increase)

    else:
        price_change = random.uniform(-max_decrease, 0)

    price *= (1 + price_change)
    day += 1

    print("on day {} price is: ${:.2f}".format(day, price), file=out_file)

out_file.close()
