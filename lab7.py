from math import sqrt

def hello(name):
    return "Hello, " + name

def square_eq_solver(a, b, c):
    result = []
    if a == 0:
        print("a = 0 -> это не квадратное уравнение!")
        return result
    discriminant = b * b - 4 * a * c
    # print("Дискриминант: ", discriminant)

    if discriminant == 0:
        result.append(round(-b / (2 * a), 2))
    # elif discriminant < 0:
    #     return result
    else:
        result.append(round((-b + sqrt(discriminant)) / (2 * a), 2))
        result.append(round((-b - sqrt(discriminant)) / (2 * a), 2))

    return result

def show_result(data):
    if len(data) > 0:
        for index, value in enumerate(data):
            print(f'Корень номер {index+1} равен {value}')
    else:
        print('Уравнение с заданными параметрами не имеет корней')

def main():
    a, b, c = map(float, input('Пожалуйста, введите три коэффициента через пробел: ').split())
    result = square_eq_solver(a, b, c)
    show_result(result)

if __name__ == '__main__':
   main()
   print(hello("kukapa sinä olet?"))
