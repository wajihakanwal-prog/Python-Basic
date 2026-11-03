team_points = [80, 90, 70, 85, 95]

last_week_points = 380

total_points = sum(team_points)

average_points = total_points / len(team_points)

reward_stars = total_points // 10

boxes = reward_stars // 5

remaining_stars = reward_stars % 5

print("Team Points:", team_points)

print("Total Points:", total_points)

print("Average Points:", average_points)

print("Reward Stars:", reward_stars)

print("Boxes:", boxes)

print("Remaining Stars:", remaining_stars)