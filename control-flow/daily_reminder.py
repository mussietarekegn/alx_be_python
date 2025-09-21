task=str(input("Enter the task description: "))
priority=str(input("Enter the task's priority(high,medium,low): "))
time_bound=str(input("Is the task in time_bound(yes or no): "))

match priority:
    case "high":
        message=f"Reminder: '{task}' is a high priority task"
    case "medium":
        message=f"Reminder: '{task}' is a medium priority task"
    case "low":
        message=f"Note : '{task}' is a low priority task"
    case _:
        message:f"'{task}' has an unknown priority level"

if time_bound=="yes":
    message+="that requires immediate attention today!"
else:
    if priority in ["high","medium"]:
        message+=". Consider completing it as soon as possible."
    else:
        message+=". Consider completing it when you have free time."
print(message)