class InvalidRangeError(Exception):
    pass

while True:
    try:
        num=int(input("Enter a number between 1 to 10:"))
        if num < 1 or num > 10:
            raise InvalidRangeError("Number must be between 1 to 10.")
        
        print("Valid Number Entered:",num)
        break
    except ValueError:
        print("Error: Please Enter a Numeric Value.")
    except InvalidRangeError as e:
        print("Error:",e)