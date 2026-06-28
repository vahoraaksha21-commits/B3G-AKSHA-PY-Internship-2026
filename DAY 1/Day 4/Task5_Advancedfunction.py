from functools import reduce
number=[21,90,45,22,29,88]

def find_largest(a,b):
    if a>b:
        return a
    else:
        return b
    
largest=reduce(find_largest,number)
print("List Of Number:",number)
print("The Largest Number in the List is:",largest)