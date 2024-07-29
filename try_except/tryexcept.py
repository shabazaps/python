def divide(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print("Cannot divide by 0!")
    else:
        print(f"Division result: {c}")
    finally:
        print("Execution Completed")


divide(10, 0)
