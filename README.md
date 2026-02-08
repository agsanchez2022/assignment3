# Command Line Calculator (Python)

This project is a robust command-line calculator built in Python using best practices, complete unit testing with pytest, and continuous integration with GitHub Actions. The application implements a REPL (Read-Eval-Print Loop) for continuous user interaction and supports addition, subtraction, multiplication, and division with full input validation and graceful error handling.

Requirements:
- Python 3.10+
- Git

Setup:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Running the Application:
python main.py

Example Commands:
add 5 3
subtract 10 4
multiply 2 6
divide 10 2
Type exit to quit.

Testing:
pytest

Test Coverage (required 100%):
pytest --cov=app --cov-report=term-missing --cov-fail-under=100

Continuous Integration:
GitHub Actions automatically runs all tests and enforces 100% coverage on every push.

Submission:
Push the project to GitHub and submit the repository link.
