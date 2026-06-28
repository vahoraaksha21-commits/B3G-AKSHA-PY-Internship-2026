username=["Aksha21","Ilma","Aafiya29","Jiya22","Mahin","Zeinab"]
valid_username=list(filter(lambda name:len(name)>=6,username))

print("username with at least 6 characters:")
print(valid_username)