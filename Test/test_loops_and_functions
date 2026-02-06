import pytest
from functions_practice import find_second_largest 

def test_second_largest_normal_case():
    numbers = [10, 45, 22, 45, 30]
    assert find_second_largest(numbers) == 45  # The second largest is 45

def test_second_largest_with_duplicates():
    numbers = [5, 5, 5, 2]
    assert find_second_largest(numbers) == 2  # The second largest is 2

def test_second_largest_sorted_numbers():
    numbers = [100, 200, 300, 400]
    assert find_second_largest(numbers) == 300

def test_second_largest_negative_numbers():
    numbers = [-10, -20, -5, -15]
    assert find_second_largest(numbers) == -10

def test_second_largest_two_numbers():
    numbers = [1, 2]
    assert find_second_largest(numbers) == 1

