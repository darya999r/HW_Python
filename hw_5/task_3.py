# 3. Создайте функцию генератор чисел Фибоначчи

def fibonacci(n: int) -> list[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(*(fibonacci(10)))