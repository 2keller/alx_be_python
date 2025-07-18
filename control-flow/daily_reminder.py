# Prompt the user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower().strip()
time_bound = input("Is it time-bound? (yes/no): ").lower().strip()

# Process the task using a match statement for priority
match priority:
    case 'high':
        # If the priority is high, the reminder is urgent.
        # The 'if' statement adds extra emphasis for time-bound tasks.
        if time_bound == 'yes':
            reminder = f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
        else:
            reminder = f"Reminder: '{task}' is a high priority task. Make sure to complete it soon."

    case 'medium':
        if time_bound == 'yes':
            reminder = f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
        else:
            reminder = f"Note: '{task}' is a medium priority task. Try to complete it today."

    case 'low':
        # For low priority, the 'if' statement determines if it's a simple note or a gentle reminder.
        if time_bound == 'yes':
            reminder = f"Note: '{task}' is a low priority task, but it needs to be completed today."
        else:
            # This case matches the example output for a non-urgent task.
            reminder = f"Note: '{task}' is a low priority task. Consider completing it when you have free time."

    case _:
        # A default case handles any invalid priority input.
        reminder = "Error: Invalid priority level entered. Please choose high, medium, or low."

# Print the final, customized reminder
print(reminder)