import sys

class FormulaError(Exception):
    pass

def calculate(formula):
    try:
        elements = formula.split()
        if len(elements) != 3:
            raise FormulaError("Invalid number of elements in the formula")
        
        num1 = float(elements[0])
        operator = elements[1]
        num2 = float(elements[2])
        
        if operator not in ('+', '-'):
            raise FormulaError("Invalid operator. Only + and - are supported")

        if operator == '+':
            result = num1 + num2
        else:
            result = num1 - num2
        
        return result
    except ValueError:
        raise FormulaError("Invalid number format in the formula")

if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise FormulaError("Usage: python calculator.py 'number operator number'")
        
        formula = sys.argv[1]
        result = calculate(formula)
        print("Result:", result)
    except FormulaError as e:
        print("Error:", e)
    except Exception as e:
        print("An unexpected error occurred:", e)
