import sys
import os

# Allow tests to import modules from the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Python_basics.conditions import weird_or_not, is_leap

# To test the givrn number is Weird or not Weird based on range 
def test_odd_number():
    # Odd numbers should always return "Weird"
    assert weird_or_not(3) == "Weird"

def test_range_2_to_5():
    # Even number in range 2-5 -> "Not Weird"
    assert weird_or_not(4) == "Not Weird"

def test_range_6_to_20():
    # Even number in range 6-20 -> "Weird"
    assert weird_or_not(8) == "Weird"

def test_greater_than_20():
    # Even number greater than 20 -> "Not Weird"
    assert weird_or_not(22) == "Not Weird"

def test_at_two():
    # test: 2 is even and within 2-5 -> "Not Weird"
    assert weird_or_not(2) == "Not Weird"

def test_at_five():
    # test: 5 is odd -> "Weird"
    assert weird_or_not(5) == "Weird"

def test_at_twenty():
    # test: 20 is even and within 6-20 -> "Weird"
    assert weird_or_not(20) == "Weird"

def test_large_even():
    # Large even number (>20) -> "Not Weird"
    assert weird_or_not(100) == "Not Weird"

def test_large_odd():
    # Large odd number -> always "Weird"
    assert weird_or_not(101) == "Weird"


# To find whether the given year is leap year or not
def test_divisible_by_400():
    # divisible by 400 -> always leap
    assert is_leap(2000) is True


def test_divisible_by_100_not_400():
    # divisible by 100 but not 400 -> NOT leap
    assert is_leap(1900) is False


def test_divisible_by_4_not_100():
    # divisible by 4 but not 100 -> leap
    assert is_leap(1996) is True


def test_not_divisible_by_4():
    # not divisible by 4 -> NOT leap
    assert is_leap(2001) is False


def test_common_leap_year():
    assert is_leap(2024) is True


def test_future_year():
    assert is_leap(2400) is True
