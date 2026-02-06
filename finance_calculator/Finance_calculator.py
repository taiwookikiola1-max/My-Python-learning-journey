"""
Finance Calculator

This module provides functions to calculate financial metrics for a business:
- Gross Profit
- Net Profit
- Current Ratio
- Debt-to-Equity Ratio

Author: Taiwo Okikiola
"""

def calculate_gross_profit(revenue: float, cogs: float) -> float:
    """
    Calculate the gross profit of a business.

    Parameters:
    revenue (float): Total revenue of the business.
    cogs (float): Cost of goods sold.

    Returns:
    float: Gross profit (revenue - cogs)
    """
    return revenue - cogs

def calculate_net_profit(gross_profit: float, operating_expenses: float) -> float:
    """
    Calculate the net profit of a business.

    Parameters:
    gross_profit (float): Gross profit amount
    operating_expenses (float): Total operating expenses

    Returns:
    float: Net profit (gross profit - operating expenses)
    """
    return gross_profit - operating_expenses

def current_ratio(current_assets: float, current_liabilities: float) -> float | None:
    """
    Calculate the current ratio, a liquidity metric.

    Parameters:
    current_assets (float): Total current assets
    current_liabilities (float): Total current liabilities

    Returns:
    float: Current ratio (current_assets / current_liabilities)
    None: If current_liabilities is zero to avoid division by zero
    """
    if current_liabilities == 0:
        return None
    return current_assets / current_liabilities

def debt_to_equity(total_liabilities: float, total_equity: float) -> float | None:
    """
    Calculate the debt-to-equity ratio.

    Parameters:
    total_liabilities (float): Total liabilities
    total_equity (float): Total equity

    Returns:
    float: Debt-to-equity ratio (total_liabilities / total_equity)
    None: If total_equity is zero to avoid division by zero
    """
    if total_equity == 0:
        return None
    return total_liabilities / total_equity

def main():
    """Main function to interactively calculate financial metrics."""
    print("=== Finance Calculator ===")
    try:
        revenue = float(input("Enter revenue: "))
        cogs = float(input("Enter cost of goods sold (COGS): "))
        gross_profit = calculate_gross_profit(revenue, cogs)
        print(f"Gross Profit: {gross_profit}")

        operating_expenses = float(input("Enter operating expenses: "))
        net_profit = calculate_net_profit(gross_profit, operating_expenses)
        print(f"Net Profit: {net_profit}")

        current_assets = float(input("Enter current assets: "))
        current_liabilities = float(input("Enter current liabilities: "))
        cr = current_ratio(current_assets, current_liabilities)
        print(f"Current Ratio: {cr if cr is not None else 'Undefined (Division by zero)'}")

        total_liabilities = float(input("Enter total liabilities: "))
        total_equity = float(input("Enter total equity: "))
        de_ratio = debt_to_equity(total_liabilities, total_equity)
        print(f"Debt-to-Equity Ratio: {de_ratio if de_ratio is not None else 'Undefined (Division by zero)'}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    main()

