# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority level"

# Check time sensitivity
if time_bound == "yes" and priority in {"high", "medium", "low"}:
    message += " that requires immediate attention today!"
elif priority in {"high", "medium", "low"}:
    message += ". Consider completing it when you have time."

# Print the final reminder
print(f"Reminder: '{task}' is a {priority} priority task" + (" that requires immediate attention today!" if time_bound == "yes" else ""))

