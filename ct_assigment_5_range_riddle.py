#CT Assignment 5- Loop Statements

#Assignment 5: Question 1
# Write a program that prints off different moods for each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", and "Calm". Using the range() function, loop through every day of the week and for each day, randomly select a mood from the list and print it.
#  Ensure that your program includes the use of the random module to select the mood.

#********************************Task 1: Version 1*************************************************

#****Start with the universal Lists that we'll use through every attempt/version

import random

days_of_the_Week = ["Monday", "Tuesday", "Wednesday", "Thrsday", "Firday", "Saturday", "Sunday"]

core_moods = ["Happy", "Sad", "Energetic", "Calm", "Manic", "Depressed", "Psychotic", "Schizophrenic", "Blank"]

#Create a loop to match a day to a mood and print out the results
print("***************************************************************************************************************")
print("***************************************First Version***********************************************************")
for day in days_of_the_Week:
    mood = random.choice(core_moods)
    print(f"On {day} the mood was {mood}")

print("***********************************End first version************************************************************")
print("*****************************************************************************************************************")

### Now we'll make one that if the mood is either Psychotic, Schizophrenic, or Manic we will take medication and alter the mood to Blank.

print("***************************************************************************************************************")
print("***************************************Alternate program with medication***************************************")
# we redo the for loop to add the new conditions and output

for day in days_of_the_Week:
    mood= random.choice(core_moods)
    #Now we check the chosen mood and do an ouput of mood matches  We set a new variable in fixed_mood so we can do more changes with the mood
    #for different medicaitons without having to change the output line (if we wanted to, which we don't right now because I'm behind schedule enough.)
    if mood in ["Psychotic", "Schizophrenic", "Manic"]:
        fixed_mood = "Blank"
        print(f"On {day} the mood was {mood} - Took medication and now my mood is {fixed_mood}")
    else:
        print(f"On {day} the mood was {mood}")

print("***********************************End second version************************************************************")
print("*****************************************************************************************************************")