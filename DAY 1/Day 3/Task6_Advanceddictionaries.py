employee={
    "Aksha" :80000,
    "Aafiya" :75000,
    "Jiya" :70000,
    "Ilma" :50000,
    "Zeinab" :60000
}
salary_list=list(employee.items())
salary_list.sort(key=lambda x:x[1],reverse=True)

print("Top 3 Highest Paid Employees:")
for A in range(3):
    print(salary_list[A][0],":",salary_list[A][1])