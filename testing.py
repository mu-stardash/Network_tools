from lab7 import hello, square_eq_solver, main
from pytest import fixture
import pytest

def test_hello():
    name = "world!"
    assert hello(name) == "Hello, world!", "Error!"

class TestClassSF:
    def test_one(self):
        x = 1
        assert x == 1 # False
    def test_two(self):
        x = 1
        assert x != 2 # True


def test_no_root():
    res = square_eq_solver(10, 0, 2)
    assert len(res) == 0, "Wrong"

def test_single_root():
    res = square_eq_solver(10, 0, 0)
    assert len(res) == 1
    assert res == [0]

def test_multiple_root():
    res = square_eq_solver(2, 5, -3)
    assert len(res) == 2
    assert res == [0.5, -3]

# @fixture
# def call_me_every_time():
#     print("Haha")

# def test_one(call_me_every_time):
#     print("Test one")

@pytest.mark.parametrize(
    ('a, b, c, expected'),[
        (10, 0, 0, [0]),
        (2, 5, -3, [0.5, -3]),
        (10, 1, 0, [0, -0.1]),
        (10, 1, 0, [0, -0.1]),
        (0, 1, 0, []),
        (-4, -2, 2, [-1, 0.5]),
        (2, 2, 2, []),
        (-100, -200, 100, [-2.41, 0.41]),
    ]
)

def test_on_range(a, b, c, expected):
    assert square_eq_solver(a, b, c) == expected
