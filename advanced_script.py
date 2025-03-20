# advanced_script.py
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def greet(name):
    if not name:
        return "Hello, World!"
    return f"Hello, {name}!"

def add(a, b):
    try:dd
        result = a + b
        logging.info(f"Addition result: {result}")
        return result
    except TypeError as e:
        logging.error(f"TypeError in add: {e}")
        return None

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    try:
        logging.info(greet("SonarQube"))
        logging.info(f"2 + 3 = {add(2, 3)}")
        logging.info(f"Factorial of 5: {factorial(5)}")
    except Exception as e:
        logging.exception("Unhandled exception occurred:", exc_info=e)
        sys.exit(1)

if __name__ == "__main__":
    main()
