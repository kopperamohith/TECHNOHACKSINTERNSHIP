def fahrentocelsius(f):
    return (f - 32) * 5.0/9.0
def celsiustofahren(c):
    return (c * 9.0/5.0) + 32
choice = input("Choose the conversion:\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\nEnter 1 or 2: ")
if choice == "1":
    f = float(input("Enter temperature in Fahrenheit: "))
    print("the fahrenheit temperature",f,"is equivalent to",fahrentocelsius(f))
elif choice == "2":
    c = float(input("Enter temperature in Celsius: "))
    print("the celsius temperature",c,"is equivalent to",celsiustofahren(c))
else:
    print("Invalid choice!")

