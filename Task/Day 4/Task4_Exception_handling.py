def read_file_safely(filename):
    try:
        with open(filename,"r")as file:
            return file.read()
    except FileNotFoundError:
        return "File Not Found"
    
print("File Content:")
print(read_file_safely("sample.txt"))

print("\nChecking Another File:")
print(read_file_safely("data.txt"))