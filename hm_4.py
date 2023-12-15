def log_function_call(func):
    def wrapper(a, b):
        function_name = func.name
        args_str = f"{a}, {b}"
        print(f"Вызвана функция {function_name} с аргументами {args_str}")
        result = func(a, b)
        print(f"Результат функции {function_name}: {result}")
        return result
    return wrapper

@log_function_call
def add(a, b):
    return a + b

@log_function_call
def multiply(a, b):
    return a * b

@log_function_call
def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль недопустимо")
    return a / b

@log_function_call
def subtract(a, b):
    return a - b

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
print()
result_add = add(a, b)
result_multiply = multiply(a, b)
result_divide = divide(a, b)
result_subtract = subtract(a, b)