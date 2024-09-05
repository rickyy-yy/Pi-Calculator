numerator = 22
denominator = 7

while True:
    try:
        degree = int(input("Enter the number of decimals: "))
        break
    except ValueError:
        pass

result = format((numerator/denominator), f".{degree}f")
print(result)
