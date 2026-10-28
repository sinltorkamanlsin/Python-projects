name = input("Enter your name: ")
is_government_job = input("Is this a government job? (yes/no): ").lower() == "yes"
yes_bool = True
no_bool = False
job = input("Enter your job: ")

monthly_salary = float(input("Enter your monthly salary: "))

tax = monthly_salary * 0.10
final_salary = monthly_salary - tax
total_salary_in_a_year = final_salary * 12

if is_government_job == yes_bool:
    income_per_hour = final_salary / 173


print("\n|-------------------------------| Salary Caculations |-------------------------------|")

print(" " + "|" + " " * 82 + "|")

print("|" + " " * 38 + "Name:", name)

print(" " + "|" + " " * 82 + "|")

print("|" + " " * 39 + "Job:", job)

print(" " + "|" + " " * 82 + "|")

print("|" + " " * 27 + "Original Salary:", str(monthly_salary) + " T")

print(" " + "|" + " " * 82 + "|")

print("|" + " " * 26 + "income TAX (10%):", str(tax) + " T")

print(" " + "|" + " " * 82 + "|")

print("|" + " " * 30 + "Final Salary:", str(final_salary) + " T")

print(" " + "|" + " " * 82 + "|")

print("|" + " " * 20 + "total salary in a year: ", str(total_salary_in_a_year) + " T")

print(" " + "|" + " " * 82 + "|")

print("|------------------------------------------------------------------------------------|")
