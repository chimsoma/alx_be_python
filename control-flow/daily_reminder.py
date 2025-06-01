# daily_reminder.py

# Get user input
task = input("Enter your task: ")

# Loop until valid priority is given
while True:
    priority = input("Priority (high/medium/low): ").lower()
    if priority in ["high", "medium", "low"]:
        break
    print("Please enter a valid priority: high, medium, or low.")

# Loop until valid time-bound response is given
while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    if time_bound in ["yes", "no"]:
        break
    print("Please enter 'yes' or 'no'.")

# Construct the reminder
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
    case "medium":
        reminder = f"'{task}' is a medium priority task"
    case "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' is a task"

# Append urgency if time-bound
if time_bound == "yes":
    reminder += " that requires immediate attention today!"

# Print the final reminder
print("\nReminder:", reminder)
