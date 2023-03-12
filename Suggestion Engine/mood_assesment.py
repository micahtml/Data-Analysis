import random

# Define our list of moods and behaviors, along with example activities
mood_behavior_activities = {
    "happy": {
        "listening to music",
        "going for a walk",
        "hanging out with friends",
        "watching a comedy movie"
    },
    "sad": {
        "taking a warm bath",
        "writing in a journal",
        "reading a favorite book",
        "watching a comforting movie"
    },
    "stressed": {
        "meditating",
        "doing some yoga",
        "taking a nap",
        "listening to calming music"
    },
    "tired": {
        "taking a power nap",
        "doing some light exercise",
        "drinking some caffeine",
        "going for a brisk walk"
    }
}

# Prompt the user to enter their mood and behavior
mood = input("How are you feeling? (happy, sad, stressed, tired): ")
behavior = input(
    "What have you been doing? (working, studying, exercising, relaxing): ")

# Check if the user's mood and behavior match any of our entries, and suggest an activity if so
if mood in mood_behavior_activities and behavior in mood_behavior_activities[mood]:
    suggestions = mood_behavior_activities[mood][behavior]
    suggestion = random.choice(list(suggestions))
    print("If you're feeling", mood, "and you've been", behavior + ", try", suggestion + "!")
else:
    print("Take a break and do something that makes you happy!")
