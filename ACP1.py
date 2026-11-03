activities = []

total_minutes = 0

num = int(input("How many activities do you perform daily? "))

for i in range(num):

    print("\nActivity", i + 1)

    activity = input("Enter activity name: ")

    minutes = int(input("How many minutes do you spend daily? "))

    weekly_minutes = minutes * 7

    activities.append({
        "name": activity,
        "daily": minutes,
        "weekly": weekly_minutes
    })

    total_minutes += weekly_minutes
    
for activity in activities:

    print("Activity:", activity["name"])
    print("Daily Time:", activity["daily"], "minutes")
    print("Weekly Time:", activity["weekly"], "minutes")
    print("-----------------------------")


print("Total weekly time:", total_minutes, "minutes")

hours = total_minutes // 60
minutes = total_minutes % 60

print("Total weekly time:", hours, "hours and", minutes, "minutes")