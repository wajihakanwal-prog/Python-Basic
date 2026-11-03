name = "Abdullah Faisal"
age = 20
club = "Computer Science Club"
member_id = 12345

print(type(name))
print(type(age))
print(type(club))
print(type(member_id))

name = str(name)
age = str(age)
club = str(club)
member_id = str(member_id)

badge_code = member_id[:4]

badge = (
    "==============================\n"
    "       SCHOOL CLUB BADGE      \n"
    "==============================\n"
    "Name: " + name + "\n"
    "Age: " + age + "\n"
    "Club: " + club + "\n"
    "Badge Code: " + badge_code + "\n"
    "=============================="
)

print(badge)