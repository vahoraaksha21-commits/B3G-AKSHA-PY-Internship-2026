def student_mark(marks):
    lowest=min(marks)
    highest=max(marks)
    average=sum(marks)/len(marks)
    return lowest,highest,average

marks=[75,82,90,68,85]
lowest_mark, highest_mark, average_mark=student_mark(marks)

print("Lowest Mark=",lowest_mark)
print("Highest Mark=",highest_mark)
print("Average Mark=",average_mark)