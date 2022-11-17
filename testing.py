from lab7 import hello, square_eq_solver, main, division, increment, decrement
from pytest import fixture
import pytest

def test_hello():
    name = "world!"
    assert hello(name) == "Hello, world!", "Error!"

class TestClassSF:
    def test_one(self):
        x = 1
        assert x != 1 # False
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



# покрываем декоратором, чтобы прогнать несколько похожих тестов в одном
@pytest.mark.parametrize("a, b, expected_result", [(10,2,5),
                                                   (20,10,2) ,
                                                   (30,-3,-10),
                                                   (5, 2, 2.5)])
def test_division_good(a,b,expected_result):
    assert division(a,b)==expected_result


def test_zero_division():
    # мы ожидаем возникновения ошибки деления на ноль
    # тест воспринимается как успешно прошедший
    with pytest.raises(ZeroDivisionError):
        # когда pytest перехватывает ошибку, он проверяет
        # параметр raises
        division(10, 0)

def test_type_error():
    # отлавливаем другое исключение
    with pytest.raises(TypeError):
        division(10, "2")

# тот же самый тест с ожиданием ошибки только универсальный
@pytest.mark.parametrize("expected_exception, divisionable, divider", [(ZeroDivisionError, 10, 0),
                                                                       (TypeError, 20, "2")])
def test_division_with_error(expected_exception, divider, divisionable):
    with pytest.raises(expected_exception):
        division(divisionable, divider)


def test_increment():
    assert increment(3) == 4

def test_decrement():
    assert decrement(3) == 2



# Фикстуры — это функции, которые будут выполняться перед каждой тестовой функцией,
# к которой они применяются. Фикстуры используются для подачи некоторых данных в тесты,
# таких как соединения с базой данных, URL-адреса для тестирования и некоторые виды входных данных.
# Поэтому вместо того, чтобы запускать один и тот же код для каждого теста, мы можем прикрепить к тестам
# функцию фиксации, и она будет запускаться и возвращать данные в тест перед выполнением каждого теста.
@pytest.fixture
def input_value():
    # Тестовая функция может использовать фикстуру, указав имя фикстуры в качестве входного параметра.
   input = 39
   return input


# Здесь у нас есть функция фиксации с именем input_value,
# которая предоставляет входные данные для тестов. Чтобы получить
# доступ к функции фикстуры, тесты должны указать имя фикстуры
# в качестве входного параметра.

# Pytest во время выполнения теста увидит имя прибора в качестве входного параметра.
# Затем он выполняет функцию фиксации, и возвращаемое значение сохраняется во входном
# параметре, который может использоваться тестом.


def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
