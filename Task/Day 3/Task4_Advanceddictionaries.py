word=["Apple","Ant","Banana","Bat","Cat","Carrot"]
group={}
for A in word:
    letter=A[0]
    group.setdefault(letter,[]).append(A)

print(group)