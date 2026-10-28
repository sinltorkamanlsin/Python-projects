
number1 = input("Enter the first number: ")
number2 = input("Enter the second number: ")

number1 = float(number1)
number2 = float(number2)

addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2
division = number1 / number2

print("                             //||||||||||||||||||||||||||||||||||||||||||||||||||||\\")
print("           //|||||||||||||||||||||                                                 |||||||||||||||||||\\")
print("                                              Addition:", addition )
print("                                              Type:", type(addition))
print("        //|||||||" + "   " * 27 + "|||||||\\")
print("                                              Subtraction:", subtraction)
print("                                              Type:", type(subtraction))
print("      ||||||||||" + "   " * 27 + "||||||||||")
print("                                              Multiplication:", multiplication)
print("                                              Type:", type(multiplication))
print("        \\|||||||" + "   " * 27 + "|||||||//")
print("                                              Division:", division)
print("                                              Type:", type(division))
print("           \\|||||||||||||||||||||                                                 |||||||||||||||||||//")
print("                             \\||||||||||||||||||||||||||||||||||||||||||||||||||||//")