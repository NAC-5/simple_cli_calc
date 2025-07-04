from calc_logic import *

def main():
    print("Welcome to the Calculator")
   
    one_arg_ops = {'sqrt', 'cbrt', '!', 'log10', 'ln', 'sin', 'cos', 'tan', 'abs', 'exp', 'pi', 'e'}
    
    print("Enter your first number: ")
    a = float(input())
    
    while True:
        print("Enter an operator: Type 'help' or 'h' for a list of available operators")
        operator = input()
        if operator == 'help' or operator == 'h':
            print("Available operators:")
            print("  +      : addition")
            print("  -      : subtraction")
            print("  *      : multiplication")
            print("  /      : division")
            print("  ^      : power (a^b)")
            print("  sqrt   : square root (of a)")
            print("  cbrt   : cube root (of a)")
            print("  !      : factorial (of a)")
            print("  log10  : log base 10 (of a)")
            print("  ln     : natural log (of a)")
            print("  sin    : sine (of a, radians)")
            print("  cos    : cosine (of a, radians)")
            print("  tan    : tangent (of a, radians)")
            print("  abs    : absolute value (of a)")
            print("  exp    : exponential (e^a)")
            print("  %      : percentage (a as % of b)")
            print("  pi     : value of pi")
            print("  e      : value of e")
            continue
        if operator not in one_arg_ops:
            print("Enter your second number: ")
            b = float(input())
        else:
            b = None
        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = subtract(a, b)
        elif operator == '*':
            result = multiply(a, b)
        elif operator == '/':
            result = divide(a, b)
        elif operator == '^':
            result = power(a, b)
        elif operator == 'sqrt':
            result = square_root(a)
        elif operator == 'cbrt':
            result = cube_root(a)
        elif operator == '!':
            if a == int(a):
                a = int(a)
                result = factorial(a)
            else:
                print("Factorial is only defined for integers")
                return
        elif operator == 'log10':
            result = log10(a)
        elif operator == 'ln':
            result = natural_log(a)
        elif operator == 'sin':
            result = sine(a)
        elif operator == 'cos':
            result = cosine(a)
        elif operator == 'tan':
            result = tangent(a)
        elif operator == 'abs':
            result = absolute(a)
        elif operator == 'exp':
            result = exponential(a)
        elif operator == '%':
            result = percentage(a, b)
        elif operator == 'pi':
            result = pi(a)
        elif operator == 'e':
            result = e(a)
        else:
            print("Invalid operator")
            continue
        print(f"Result: {result}")
        break

if __name__ == "__main__":
    main()
