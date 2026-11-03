app_name = input("Enter app name: ")
student_age = int(input("Enter student age: "))

approved_apps = ["WhatsApp", "YouTube", "Google", "Facebook"]
restricted_apps = ["TikTok", "PUBG", "Instagram"]

print("\nData Type Checking:")

if isinstance(app_name, str) and isinstance(student_age, int):
    print("Data types are correct.")
else:
    print("Invalid data types.")

print("\nApp Access Checking:")

if app_name in restricted_apps:
    print("Access Denied! This app is restricted.")

elif app_name in approved_apps:
    print("Access Granted! This app is approved.")

else:
    print("App is not in the approved list.")

VIEW = 1
DOWNLOAD = 2
SHARE = 4

print("\nApp Permissions:")

print("VIEW:", bin(VIEW))
print("DOWNLOAD:", bin(DOWNLOAD))
print("SHARE:", bin(SHARE))

permissions = VIEW | DOWNLOAD

print("\nCombined Permissions:")
print("Permissions:", permissions)
print("Binary:", bin(permissions))

print("\nTesting Permissions:")

if permissions & VIEW:
    print("View Permission: Allowed")

if permissions & DOWNLOAD:
    print("Download Permission: Allowed")

if permissions & SHARE:
    print("Share Permission: Allowed")

print("\nBitwise Shift Operations:")

print("Left Shift:", permissions << 1)
print("Right Shift:", permissions >> 1)