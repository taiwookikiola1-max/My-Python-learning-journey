
   """
Profit margin Calculator

This script calculates gross profit, gross profit margin, operating profit, operating profit margin 
based on user inputs.

Author: Taiwo Okikiola
"""



def calc_gross_profit(revenue, cogs):
    if revenue == 0:
        return 0
    return revenue - cogs

# revenue is the total income generated in the accounting / fiscal year
# cogs is the total cost of goods sold during the period in question



def calc_gross_profit_margin(revenue, cogs):
    if revenue == 0:
        return 0
    return (revenue - cogs) / revenue * 100


def calc_operating_profit(gross_profit, operating_expenses):
    return gross_profit - operating_expenses

# operating expenses are the expenses incurred during the said period

def calc_operating_profit_margin(operating_profit, revenue):
    if revenue == 0:
        return 0
    return (operating_profit / revenue) * 100


def main():
    revenue = float(input("Enter revenue: "))
    cogs = float(input("Enter cost of goods sold (COGS): "))
    operating_expenses = float(input("Enter operating expenses: "))

    gross_profit = calc_gross_profit(revenue, cogs)
    print(f"Gross profit: {gross_profit:.2f}")
    print(f"Gross profit margin: {calc_gross_profit_margin(revenue, cogs):.2f}%")

    operating_profit = calc_operating_profit(gross_profit, operating_expenses)
    print(f"Operating profit: {operating_profit:.2f}")
    print(
        f"Operating profit margin: "
        f"{calc_operating_profit_margin(operating_profit, revenue):.2f}%" )


if __name__ == "__main__":
    main()
