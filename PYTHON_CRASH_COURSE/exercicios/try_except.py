def zero_division_Error():
    try:
        print(5/0)
    except ZeroDivisionError:
        print("You can't divide by zero!")


zero_division_Error()