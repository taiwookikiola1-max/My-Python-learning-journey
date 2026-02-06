import pytest
from Finance_calculator import (
    calculate_gross_profit,
    calculate_net_profit,
    current_ratio,
    debt_to_equity
)

def test_calculate_gross_profit():
    assert calculate_gross_profit(1000, 400) == 600
    assert calculate_gross_profit(0, 0) == 0

def test_calculate_net_profit():
    assert calculate_net_profit(600, 200) == 400
    assert calculate_net_profit(0, 0) == 0

def test_current_ratio():
    assert current_ratio(1000, 500) == 2
    assert current_ratio(1000, 0) is None  # division by zero

def test_debt_to_equity():
    assert debt_to_equity(500, 1000) == 0.5
    assert debt_to_equity(500, 0) is None  # division by zero

