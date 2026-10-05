habits = [
    ("Drink water", True),
    ("Read 10 pages", False),
    ("Exercise", True),
    ("Sleep 8 hours", True)
]

for habit, completed in habits:
    if completed:
        print(habit + ": Done")
    else:
        print(habit + ": Not done")


def habit_report(habits):
    completed_count = 0

    for habit, completed in habits:
        if completed:
            completed_count += 1

    return {
        "completed": completed_count,
        "total": len(habits)
    }


print(habit_report(habits))