
# moodtracker

print("Welcome to the Mood Tracker!", "\nPlease enter your mood for each day of the week.")
print("You can enter multiple moods (happy, sad, stressed, neutral).") 
print("Please enter your mood for each day of the week.")
print("You can choose from: happy, sad, stressed, neutral\n")

# list of moods to validate
valid_moods = ["happy", "sad", "stressed", "neutral"]

# days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# dictionary to store results
mood_log = {}

for day in days:
    while True:
        mood = input(f"Enter your mood for {day}: ").lower().strip()
        if mood in valid_moods:
            mood_log[day] = mood
            break
        else:
            print("Invalid mood. Please enter one of:", ", ".join(valid_moods))

print("\n✅ Mood Tracking Complete! Here’s your week:")
for day, mood in mood_log.items():
    print(f"{day}: {mood}")

# Calculate mood percentages
mood_counts = {mood: 0 for mood in valid_moods}
for mood in mood_log.values():
    mood_counts[mood] += 1       

print("\n📊 Mood Percentages:")
for mood, count in mood_counts.items():
    percentage = (count / len(days)) * 100
    print(f"{mood.capitalize()}: {percentage:.1f}%")                                               
