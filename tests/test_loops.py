import sys
import os

# Allow importing from parent folder
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Python_basics.loops import squares_upto, concat_numbers   

# square roots
def test_zero():
    # Test: when input is 0, the function should return an empty list
    assert squares_upto(0) == []

def test_one():
    # Test: when input is 1, only 0² fits, so output should be [0]
    assert squares_upto(1) == [0]

def test_five():
    # Test: when input is 5, squares from 0² to 4² must be returned
    assert squares_upto(5) == [0, 1, 4, 9, 16]

def test_two():
    # Test: when input is 2, squares 0² and 1² only fit
    assert squares_upto(2) == [0, 1]

def test_ten():
    # Test: when input is 10, return list of squares of 0 to 9
    assert squares_upto(10) == [i*i for i in range(10)]

def test_negative():
    # Test: negative input should return an empty list
    assert squares_upto(-5) == []

# concat numbers
def test_small_number():
    # Test: for small n=3, concatenate 1,2,3 -> "123"
    assert concat_numbers(3) == "123"

def test_single_number():
    # Test: for n=1, output should be just "1"
    assert concat_numbers(1) == "1"

def test_medium_number():
    # Test: for medium n=5, output must be "12345"
    assert concat_numbers(5) == "12345"

def test_zero():
    # Test: for n=0, no numbers to concatenate -> empty string
    # n=0 -> no output
    assert concat_numbers(0) == ""

def test_large_number():
    # Test: large n=10 should give "12345678910"
    assert concat_numbers(10) == "12345678910"    