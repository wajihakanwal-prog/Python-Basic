can_swim = input("Can you swim? (yes/no): ").lower()

passed_test = input("Have you passed the swimming test? (yes/no): ").lower()

if can_swim == "yes" and passed_test == "yes":
    print("You are allowed to enter the deep end.")

elif can_swim == "yes" and passed_test == "no":
    print("You can enter the shallow end only.")

elif can_swim == "no" or passed_test == "no":
    print("You are allowed to enter the shallow end only.")

else:
    print("Invalid input. Please enter yes or no.")

print("Stay safe and follow pool rules!")