temperature=int(input("Enter the temperature in Fahrenheit: "))
if temperature <20:
    print("It is very cold")
elif temperature <40:
    print("It is cold")
elif temperature <60:
    print("It is mild")
elif temperature <80:
    print("It is warm")
else:
    print("It is very warm")
is_raining = input("Is it raining? (yes/no): ")
if is_raining == "yes":
    print("Take an umbrella")
else:
    print("No need to take an umbrella")
if is_raining == "yes" and temperature < 40:
    print("It is raining and cold, so take an umbrella and wear warm clothes")
elif is_raining == "yes" and temperature >= 40:
    print("It is raining and warm, so take an umbrella and wear light clothes")
elif is_raining == "no" and temperature < 40:
    print("It is not raining and cold, so wear warm clothes")
else:
    print("It is not raining and warm, so wear light clothes")

wind_speed = int(input("Enter the wind speed in miles per hour: "))
if wind_speed < 5:
    print("No need to wear a jacket")
elif wind_speed < 15:
    print("Wear a light jacket")
else:
    print("Wear a heavy jacket")
has_puddle=input("Is there a puddle on the ground? (yes/no): ")
if has_puddle == "yes":
    print("Be careful not to slip")
else:
    print("No need to be careful")
print("Temperature: ", temperature)
print("Wind speed: ", wind_speed)
print("Has puddle: ", has_puddle)
