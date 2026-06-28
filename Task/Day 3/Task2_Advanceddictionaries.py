student = [
    {"name": "Aksha", "marks":95},
    {"name": "Aafiya", "marks":93},
    {"name": "Jiya", "marks":90}
]
highest_mark=0
top_student=""
for i in student:
    if i["marks"] > highest_mark:
        highest_mark=i["marks"]
        top_student=i["name"]

print("Top Student:",top_student)
print("Highest Marks:",highest_mark)