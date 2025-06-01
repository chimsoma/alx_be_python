# daily_reminder.py

# Prompt for task info
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        reminder = f"Reminder: '{task}' has an unknown priority level"

# Modify reminder if time-bound
if time_bound == "yes" and priority in {"high", "medium", "low"}:
    reminder += " that requires immediate attention today!"
elif priority in {"high", "medium", "low"}:
    reminder += ". Consider completing it when you have free time."

print(reminder)
