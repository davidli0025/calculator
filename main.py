import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator_pro():
    print(art.logo)
    try:
        num1 = float(input("What's the first number?:"))
    except ValueError:
        print("number only!!!")
        calculator_pro()

    for symbol in operation:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation:  ")
        try:
            num2 = float(input("What's the second number?:"))
        except ValueError:
            print("number only..")
            continue
        calculation_func = operation[operation_symbol]
        result = calculation_func(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")
        if input(f"Want to  continue calculating with {result}: 'yes' or 'no' ") == 'yes':
            num1 = result

        else:
            should_continue = False
            calculator_pro()


calculator_pro()
