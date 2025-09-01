import math

try:
    operator = input("Enter an operator (+ - * / ^ sqrt log fact) : ").strip().lower()
    num1 = float(input("Enter the 1st number : "))

    if operator not in ["sqrt", "fact", "log"]:
        num2 = float(input("Enter the 2nd number : "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "^":  # power
        result = math.pow(num1, num2)
    elif operator == "sqrt":
        result = math.sqrt(num1)
    elif operator == "log":
        result = math.log(num1)  
    elif operator == "fact":
        result = math.factorial(int(num1))  
    else:
        print(f"❌ '{operator}' is not a valid operator.")
        result = None

    if result is not None:
        print("✅ Result:", round(result, 3))

except ZeroDivisionError:
    print("⚠️ Error: Division by zero is not allowed.")
except ValueError:
    print("⚠️ Error: Invalid number entered.")
except Exception as e:
    print(f"⚠️ Unexpected error: {e}")
