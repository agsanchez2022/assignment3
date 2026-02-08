from app.operations import addition, subtraction, multiplication, division


def calculator(input_fn=input, output_fn=print) -> None:
    output_fn("Welcome to the calculator REPL! Type 'exit' to quit")

    while True:
        user_input = input_fn(
            "Enter an operation (add, subtract, multiply, divide) and two numbers, or 'exit' to quit: "
        )

        if user_input.lower().strip() == "exit":
            output_fn("Exiting calculator...")
            break

        try:
            operation, num1, num2 = user_input.split()
            num1, num2 = float(num1), float(num2)
        except ValueError:
            output_fn("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue

        if operation == "add":
            result = addition(num1, num2)
        elif operation == "subtract":
            result = subtraction(num1, num2)
        elif operation == "multiply":
            result = multiplication(num1, num2)
        elif operation == "divide":
            try:
                result = division(num1, num2)
            except ValueError as e:
                output_fn(str(e))
                continue
        else:
            output_fn(
                f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide."
            )
            continue

        output_fn(f"Result: {result}")
