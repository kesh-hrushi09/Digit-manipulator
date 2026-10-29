user = int(input("Enter a 3 digit number: "))

hundreds = int(user // 100)
remainding  = user % 100
tens = remainding // 10
units = remainding % 10
total = hundreds + tens + units

print(total)
print(hundreds)
print(tens)
print(units)

