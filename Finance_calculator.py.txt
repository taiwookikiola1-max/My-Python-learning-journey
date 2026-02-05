def calculate_gross_profit(revenue, cogs):
    return revenue - cogs


def calculate_net_profit(gross_profit, operating_expenses):
    return gross_profit - operating_expenses

def current_ratio(current_assets, current_liabilities):
    if current_liabilities == 0:
        return None
    return current_assets / current_liabilities


def debt_to_equity(total_liabilities, total_equity):
    if total_equity == 0:
        return None
    return total_liabilities / total_equity

def profit_menu():
    revenue = float(input("Enter revenue: "))
    cogs = float(input("Enter COGS: "))
    operating_expenses = float(input("Enter operating expenses: "))

    gross = calculate_gross_profit(revenue, cogs)
    net = calculate_net_profit(gross, operating_expenses)

    print("\n--- Profit Summary ---")
    print("Gross Profit:", round(gross, 2))
    print("Net Profit:", round(net, 2))


def ratios_menu():
    current_assets = float(input("Enter current assets: "))
    current_liabilities = float(input("Enter current liabilities: "))
    total_liabilities = float(input("Enter total liabilities: "))
    total_equity = float(input("Enter total equity: "))

    cr = current_ratio(current_assets, current_liabilities)
    dte = debt_to_equity(total_liabilities, total_equity)

    print("\n--- Financial Ratios ---")
    print("Current Ratio:", "Invalid" if cr is None else round(cr, 2))
    print("Debt-to-Equity Ratio:", "Invalid" if dte is None else round(dte, 2))


def main():
    while True:
        print("\n=== Finance Calculator ===")
        print("1. Calculate Profit")
        print("2. Calculate Financial Ratios")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            profit_menu()
        elif choice == "2":
            ratios_menu()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()


