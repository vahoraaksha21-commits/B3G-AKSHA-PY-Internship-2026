count=0

def call_counter():
    global count
    count += 1
    print("Function Called",count,"time(Aksha)")
call_counter()
call_counter()
call_counter()
call_counter()
call_counter()

print("\nFinal Count=",count)