default_setting={
    "theme":"light",
    "language":"English",
    "notification":True 
}
user_setting={
    "theme":"dark",
    "notification":False
}
final_setting=default_setting.copy()
for key in user_setting:
    final_setting[key]=user_setting[key]

print(final_setting)