apple_price = 100
banana_price = 50
milk_price = 200
bread_price = 150

apple_qty = 2
banana_qty = 3
milk_qty = 1
bread_qty = 2

total_bill = apple_price * apple_qty + banana_price * banana_qty + milk_price * milk_qty + bread_price * bread_qty

discount = total_bill * 10 / 100
final_bill = total_bill - discount


print("Total Bill:", total_bill)
print("Discount:", discount)
print("Final Bill:", final_bill)

print("\nDivisibility Checking")

if final_bill % 2 == 0:
    print("Bill is divisible by 2")
else:
    print("Bill is not divisible by 2")

if final_bill % 5 == 0:
    print("Bill is divisible by 5")
else:
    print("Bill is not divisible by 5")

print("\nCorrecting Mean")

prices = [100, 50, 200, 150]
wrong_price = 100
correct_price = 150

old_mean = sum(prices) / len(prices)

corrected_total = sum(prices) - wrong_price + correct_price
corrected_mean = corrected_total / len(prices)

print("Old Mean:", old_mean)
print("Corrected Mean:", corrected_mean)

print("\nBudget Comparison")

budget1 = 1000
budget2 = 1500
budget3 = 2000

print("Budget 1:", final_bill <= budget1)
print("Budget 2:", final_bill <= budget2)
print("Budget 3:", final_bill <= budget3)


print("Total Bill       |", total_bill)
print("Discount         |", discount)
print("Final Bill       |", final_bill)
print("Old Mean         |", old_mean)
print("Corrected Mean   |", corrected_mean)
print("Budget 1000      |", final_bill <= budget1)
print("Budget 1500      |", final_bill <= budget2)
print("Budget 2000      |", final_bill <= budget3)
