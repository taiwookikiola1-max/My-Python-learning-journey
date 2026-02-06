def calc_current_ratio(current_assets, current_liabilities):
    if current_liabilities == 0:
        return None
    return current_assets / current_liabilities


def calc_debt_to_equity_ratio(total_liabilities, total_equity):
    if total_equity == 0:
        return None
    return total_liabilities / total_equity


def main():
    current_assets = float(input("Enter current assets: "))
    current_liabilities = float(input("Enter current liabilities: "))
    total_liabilities = float(input("Enter total liabilities: "))
    total_equity = float(input("Enter total equity: "))

    current_ratio = calc_current_ratio(current_assets, current_liabilities)
    debt_to_equity_ratio = calc_debt_to_equity_ratio(total_liabilities, total_equity)

    print("\n--- Financial Ratios Summary ---")

    if current_ratio is None:
        print("Current Ratio: Cannot divide by zero")
    else:
        print("Current Ratio:", round(current_ratio, 2))

    if debt_to_equity_ratio is None:
        print("Debt-to-Equity Ratio: Cannot divide by zero")
    else:
        print("Debt-to-Equity Ratio:", round(debt_to_equity_ratio, 2))


if __name__ == "__main__":
    main()
