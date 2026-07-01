class InvalidAgeError(Exception):
    pass

def register_user(age):
    if age < 0:
        raise InvalidAgeError("Age Cannot be Below 0.")
    elif age > 120:
        raise InvalidAgeError("Age Cannot be Above 120.")
    else:
        return f"User Registered Successfully with Age {age}"
    
try:
    print(register_user(21))
    print(register_user(150))
except InvalidAgeError as e:
    print("Error:",e)