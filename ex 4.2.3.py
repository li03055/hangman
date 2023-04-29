temperature = input("Enter a temperature to convert: ")
if temperature[-1] == 'C' or temperature[-1] == 'c':
    converted_temperature_f = (9 * float(temperature[:-1]) + 32 * 5) / 5
    print(converted_temperature_f, "Fahrenheit")
elif temperature[-1] == 'F' or temperature[-1] == 'f':
    converted_temperature_c = (5 * float(temperature[:-1]) - 160) / 9
    print(converted_temperature_c, "Celsius")
else:
    print("NOT")