"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months = int(input("How many months? "))

    for month_scaler in range(1, months + 1):
        income = float(input("Enter income for month " + str(month_scaler) + ": "))
        incomes.append(income)

    print("\nIncome Report\n-------------")
    total = 0
    for month_scaler in range(1, months + 1):
        income = incomes[month_scaler - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month_scaler, income, total))


main()