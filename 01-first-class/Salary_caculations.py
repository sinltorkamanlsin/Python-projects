# updated not finished still has a bug


name = input("Enter your name: ")
is_government_job = input("Is this a government job? (yes/no): ").lower() == "yes"
job = input("Enter your job: ")
name = input("Enter your name: ")
is_government_job = input("Is this a government job? (yes/no): ").lower() == "yes"
job = input("Enter your job: ")

monthly_salary = float(input("Enter your monthly salary: "))

if monthly_salary > 50000000:
    tax_percentage = 20
    tax = monthly_salary * 0.20
elif monthly_salary > 35000000:
    tax_percentage = 15
    tax = monthly_salary * 0.15
elif monthly_salary > 10000000:
    tax_percentage = 10
    tax = monthly_salary * 0.10
else:
    tax_percentage = 0
    tax = 0

final_salary = monthly_salary - tax
total_salary_in_a_year = final_salary * 12

if is_government_job:
    income_per_hour = final_salary / 173

print(f"""
|{('-'*25).ljust(25)}{'Salary Caculations'.center(20)}{('-'*25).rjust(25)}|
|{('Name: '+name).center(70)}|
|{('Job: '+job).center(70)}|
|{('Original Salary: '+str(monthly_salary)+' T').center(70)}|
|{('income TAX ('+str(tax_percentage)+'%): '+str(tax)+' T').center(70)}|
|{('Final Salary: '+str(final_salary)+' T').center(70)}|
|{('total salary in a year: '+str(total_salary_in_a_year)+' T').center(70)}|
|{('-'*70).center(70)}|
""")
# print("\n|-------------------------------| Salary Caculations |-------------------------------|")

# print(" " + "|" + " " * 82 + "|")

# print("|" + " " * 38 + "Name:", name)

# print(" " + "|" + " " * 82 + "|")

# print("|" + " " * 39 + "Job:", job)

# print(" " + "|" + " " * 82 + "|")

# print("|" + " " * 27 + "Original Salary:", str(monthly_salary) + " T")

# print(" " + "|" + " " * 82 + "|")

# print("|" + " " * 26 + "income TAX (10%):", str(tax) + " T")

# print(" " + "|" + " " * 82 + "|")

# print("|" + " " * 30 + "Final Salary:", str(final_salary) + " T")

# print(" " + "|" + " " * 82 + "|")

# print("|" + " " * 20 + "total salary in a year: ", str(total_salary_in_a_year) + " T")

# print(" " + "|" + " " * 82 + "|")

# print("|------------------------------------------------------------------------------------|")
