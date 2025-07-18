from difflib import Match

task = input("describe the task: ")
time_bound = input("is the task time bound,YES and  NO ")
priority = input("choose task priority,high, medium, low: ")

match priority | time_bound:
    case "high" | "yes":
        print("Reminder: finish",task ,"is a high priority task that requires immediate attention today!")
    case "medium"| "no":
        print(task, 'is a low priority task. Consider completing it when you have free time.')