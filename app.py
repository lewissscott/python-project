def add(a: float, b: float) -> float:
    return a + b
 
 
def subtract(a: float, b: float) -> float:
    return a - b
 
 
def multiply(a: float, b: float) -> float:
    return a * b
 
 
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
 
 
def calculate(operation: str, a: float, b: float) -> float:
    ops = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: '{operation}'. Choose from: {list(ops.keys())}")
    return ops[operation](a, b)
 
 
if __name__ == "__main__":
    print("Simple Calculator")
    print("-" * 20)
    examples = [
        ("add", 10, 5),
        ("subtract", 10, 5),
        ("multiply", 10, 5),
        ("divide", 10, 5),
    ]
    for op, a, b in examples:
        result = calculate(op, a, b)
        print(f"{op}({a}, {b}) = {result}")
