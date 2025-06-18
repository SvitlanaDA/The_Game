print("The temperature description")
temperature  = int(input("Enter temperature : "))
temperature = "Cold" if temperature < 15  else "Hot" if temperature > 30 else "Warm"
print(temperature)