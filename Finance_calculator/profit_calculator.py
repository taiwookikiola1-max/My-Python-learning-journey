def calculate_gross_profit(revenue, cogs):
    if revenue <= 0 or cogs <= 0:
        return 0
    else:
        return revenue - cogs


def calculate_net_profit(gross_profit, operating_expenses):
    if operating_expenses <= 0:
        print("Values cannot be negative or zero.")

    return gross_profit - operating_expenses




def main():
    revenue = float(input("Enter total revenue: "))
    cogs = float(input("Enter cost of goods sold (COGS): "))
    operating_expenses = float(input("Enter operating expenses: "))

    gross_profit = calculate_gross_profit(revenue, cogs)
    net_profit = calculate_net_profit(gross_profit, operating_expenses)

    if revenue < 0 or cogs < 0 or operating_expenses < 0:
        print("Values cannot be negative.")
        return

    print("\n--- Profit Summary ---")
    print("Gross Profit:", gross_profit)
    print("Net Profit:", net_profit)

if __name__ == '__main__':
    main()

