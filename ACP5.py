homework_time = int(input("Enter your homework time (hours): "))
free_time = int(input("Enter your free time (hours): "))

if homework_time >= 3:
    print("\nDaily Activity Plan")
    print("Complete your homework first.")
    print("Take a short break.")
else:
    print("\nDaily Activity Plan")
    print("Complete your homework.")
    print("Revise your lessons.")

if free_time >= 2:
    print("Enjoy outdoor games or hobbies.")
    print("Spend time with family.")
else:
    print("Use your free time wisely.")
    print("Read a book or relax.")

print("\nYour daily plan is ready!")