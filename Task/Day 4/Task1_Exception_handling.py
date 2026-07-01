def safe_division(a,b):
    try:
        result=a/b
        return result
    except ZeroDivisionError:
        return "Error: Division by Zero is not allowed."
    except TypeError:
        return "Error: Please Enter Numeric Values Only."
    
print(safe_division(20,2))
print(safe_division(20,0))
print(safe_division(20,"5"))