# daily_reminder.py

# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match-case based on priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' has an unknown priority level"

# Append time-sensitivity info
if time_bound == "yes" and priority in {"high", "medium", "low"}:
    message += " that requires immediate attention today!"
elif priority in {"high", "medium", "low"}:
    message += ". Consider completing it when you have free time."

# Print the final reminder
print(message)
