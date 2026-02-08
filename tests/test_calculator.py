from app.calculator import calculator

def test_calculator_exit_only(capsys):
    inputs = iter(["exit"])
    calculator(input_fn=lambda _: next(inputs), output_fn=print)
    out = capsys.readouterr().out
    assert "Welcome to the calculator REPL!" in out
    assert "Exiting calculator..." in out

def test_calculator_valid_add_then_exit(capsys):
    inputs = iter(["add 2 3", "exit"])
    calculator(input_fn=lambda _: next(inputs), output_fn=print)
    out = capsys.readouterr().out
    assert "Result:" in out
    assert "5" in out  # allows 5 or 5.0

def test_calculator_invalid_input_then_exit(capsys):
    inputs = iter(["badinput", "exit"])
    calculator(input_fn=lambda _: next(inputs), output_fn=print)
    out = capsys.readouterr().out
    assert "Invalid input. Please follow the format" in out

def test_calculator_unknown_operation_then_exit(capsys):
    inputs = iter(["power 2 3", "exit"])
    calculator(input_fn=lambda _: next(inputs), output_fn=print)
    out = capsys.readouterr().out
    assert "Unknown operation" in out

def test_calculator_divide_by_zero_then_exit(capsys):
    inputs = iter(["divide 1 0", "exit"])
    calculator(input_fn=lambda _: next(inputs), output_fn=print)
    out = capsys.readouterr().out
    assert "Division by zero is not allowed." in out

def test_calculator_subtract_then_exit(capsys):
    inputs = iter(["subtract 5 3", "exit"])
    calculator(input_fn=lambda _: next(inputs), output_fn=print)
    out = capsys.readouterr().out
    assert "Result:" in out
    assert "2" in out  # allows 2 or 2.0


def test_calculator_multiply_then_exit(capsys):
    inputs = iter(["multiply 2 4", "exit"])
    calculator(input_fn=lambda _: next(inputs), output_fn=print)
    out = capsys.readouterr().out
    assert "Result:" in out
    assert "8" in out  # allows 8 or 8.0




