def create_frozenset(items):
    return frozenset(items)
number=[10,20,30,40,50]
result=create_frozenset(number)

print("Frozenset:",result)
print(type(result))