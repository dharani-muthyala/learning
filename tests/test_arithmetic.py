import sys
import os

# Allow importing from parent folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Python_basics.arithmetic import arithmetic_ops, division_results


def test_sum():
    # 3 + 2 = 5
    assert arithmetic_ops(3, 2)[0] == 5


def test_difference():
    # 3 - 2 = 1
    assert arithmetic_ops(3, 2)[1] == 1


def test_product():
    # 3 * 2 = 6
    assert arithmetic_ops(3, 2)[2] == 6


def test_negative_numbers():
    # -4 + 2 = -2, -4 - 2 = -6, -4 * 2 = -8
    assert arithmetic_ops(-4, 2) == (-2, -6, -8)


def test_zero():
    # 0 + 10 = 10, 0 - 10 = -10, 0 * 10 = 0
    assert arithmetic_ops(0, 10) == (10, -10, 0)


def test_large_numbers():
    # Large integer handling
    assert arithmetic_ops(100000, 200000) == (300000, -100000, 20000000000)


# Division results

def test_simple_division():
    assert division_results(10, 2) == (5, 5.0)


def test_non_exact_division():
    assert division_results(7, 3) == (2, 7/3)


def test_division_by_larger_number():
    assert division_results(3, 5) == (0, 3/5)


def test_negative_values():
    assert division_results(-10, 3) == (-4, -10/3)


def test_both_negative():
    assert division_results(-9, -4) == (2, 2.25)


def test_zero_numerator():
    assert division_results(0, 7) == (0, 0.0)


def test_division_by_zero():
    try:
        division_results(5, 0)
        assert False   # should not reach here
    except ZeroDivisionError:
        assert True