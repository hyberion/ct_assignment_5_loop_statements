#CT Assignment 5- Loop Statements

#Assignment 5: Question 2
# Simulate a mood tracker that records your mood at three different times of the day (morning, afternoon, evening) for each day of the week. Use nested loops to implement this: the outer loop should iterate over the days, and the inner loop should iterate over the times of the day. For each time, randomly select a mood from a predefined list and print it. 
# Use the random module again to randomly select the mood.

#********************************Task 1: Version 1*************************************************

#****Start with the universal Lists that we'll use through every attempt/version

import random

#Days of the week
days_of_the_Week = ["Monday", "Tuesday", "Wednesday", "Thrsday", "Firday", "Saturday", "Sunday"]
#Times of day list
times_of_day = ["Morning", "Afternoon", "Evening"]
#List of core moods
core_moods = ["Happy", "Sad", "Energetic", "Calm", "Manic", "Depressed", "Psychotic", "Schizophrenic", "Blank"]

#Create a loop to match a day to a mood and print out the results
print("***************************************************************************************************************")
print("***************************************First Version***********************************************************")
for day in days_of_the_Week:
    print (f"\n{day}:")
    for time in times_of_day:
        current_mood = random.choice(core_moods)
        print (f"     {time}: {current_mood}")

print("***********************************End first version************************************************************")
print("*****************************************************************************************************************")
# Second Version
print("***************************************************************************************************************")
print("***************************************Second Version***********************************************************")
# NOw lets add treatment and adjustments
# We create a list of energizing activities and calming activities.  If the mood is either Manic or Dpressed we choose an 
#appropriate treatment and print out the adjusted mood.
# Yes  I know this is kinda nutty but trust me, if you think it's annoying you should try living with it.
# All hail the omnisiaah.

#We add the new lists

calming_activities = ["Medication", "Listened to soft music", "Breathing Exercises", "Yoga", "Repeated concussive blows to the head"]
energetic_activities = ["dancing", "Went on a run", "Heavy Metal Music!", "Sports", "Did a workout", "Random violence" ]

#Now we tangle some loops together and see what happens

for day in days_of_the_Week:
    print(f"\n {day}")
    for time in times_of_day:
        mood = random.choice(core_moods)

        if mood == "Manic":
            activity = random.choice(calming_activities)
            new_mood = "Calm"
            print(f"   {time}: {mood} - Did {activity} to calm down, now mood is {new_mood}.")
        elif mood == "Depressed":
            activity = random.choice(energetic_activities)
            new_mood = "Happy"
            print(f"   {time}: {mood} - Did {activity} to perk up, now mood is {new_mood}.")
        else:
            print(f"     {time}: {mood}")
print("***********************************End second version************************************************************")
print("*****************************************************************************************************************")