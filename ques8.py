def fahrenheit_to_celsius(fahrenheit):
    celsius = (5/9) * (fahrenheit - 32)
    return celsius

fahrenheit=float(input("enter the temperature: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print(f"the temp in fahrenheit is {fahrenheit} and after converting to celsius it is {celsius:2f}")