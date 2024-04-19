def calculate(expression: str) -> int:
    try:
        a, op, b = expression.split()
        a = int(a)
        b = int(b)
        if not (1 <= abs(a) <= 10 and 1 <= abs(b) <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10 включительно")

        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b == 0:
                raise ValueError("Деление на ноль")
            result = a // b
        else:
            raise ValueError("Неподдерживаемая операция")

        return result
    except ValueError as e:
        return str(e)


def main(expression: str) -> None:
    while True:
        try:
            expression = input("Введите выражение: ")
            result = calculate(expression)
            return str(result)
        except ValueError as e:
            print("Ошибка:", e)
            raise SystemExit(1)
            return str(result)


if __name__ == '__main__':
    result = main("") # необходимо передать пустую строку
    print("Результат:", result)
