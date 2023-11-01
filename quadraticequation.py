a = float(input("a="))
b = float(input("b="))
c = float(input("c="))

def solve_quadratic_equation(a, b, c):
    print(f"{a}*x*x + {b}*x + {c}")

    d = b**2 - 4*a*c
    x1 = (-b + d**0.5)/(2*a)
    x2 = (-b - d**0.5)/(2*a)
    result = f"K= {x1}, {x2}"

    return result

print(solve_quadratic_equation(a, b, c))