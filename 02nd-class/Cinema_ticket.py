age = int(input("Enter your age: "))
movie = input("What movie do you want to watch? ")

if age < 5:
    price = "FREE"
elif age <= 18:
    price = 15
elif age <= 60:
    price = 100
else:
    price = 70

print(f"""
{"_"} {" " * 42} {"_"}
{"-" * 46}
                MOVIE TICKET
{"-" * 46}
Movie: {movie}
Age: {age}
Ticket price: {price}
{"-" * 46}
{"_"} {"//\\//\\" * 7} {"_"}
""")
