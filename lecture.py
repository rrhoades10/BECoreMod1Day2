# T || T == T
# T && T == T
# T and F == F
# T or F == T
# F and F == F

torch_lit = True #True is a boolean

if torch_lit:
    print("Venture forth into the cave!")

if torch_lit == True:
    print("Go light the way!")

# combining conditionals
gold_coins = 10
silver_coins = 50
if gold_coins > 5 and silver_coins > 30:
    print("Yay you have enough to buy the magic potion!")

# both need to be true in order to execute
if gold_coins > 15 and silver_coins > 30:
    print("Cool you can buy some new armor!")

# Not Conditions if this is not equal to this then do that
enemy = "goblin"
if enemy != "dragon":
    print("Charge forward, the foe is weak!")

enemy = "dragon"
if enemy == "dragon":
    print("be careful hes cranky")

# Greater and Lesser Conditions
player_health = 25
if player_health < 100:
    print("You better drink a potion or you're gonna die!")

player_health = 40
if player_health >= 75:
    print("It looks like you're doin ok, you can hold off for now!")

# Checking Ranges num < num2 < num3
magic_stones = 30
if 10 <= magic_stones <= 20:
    print("You've unlocked the cool secret treasure chest")

# using and for a range
if magic_stones >= 10 and magic_stones <= 20:
    print("You unlocked the chest, great job!")
# needing at least 10 stones to open the chest
if magic_stones >= 10:
    print("You got the chest!")

# Negative Checks
is_daytime = False
dragon_asleep = True

if dragon_asleep:
    print("Go into the lair")
if not is_daytime: # if it is not day_time -> is_daytime as a variable has a Falsey value or is False, it is true that it is false
    print("Go to sleep!")

if not is_daytime and dragon_asleep:
    print("Sneak in to the dragon's lair and grab some of that sweet, sweet loot")

if is_daytime == True and dragon_asleep == True:
    print("Go sneak!")

# ELIF -> else if
moon_phase = "full moon"

if moon_phase == "regular moon" or moon_phase == "full moon":
    print("Beware of Werewolves!")
elif moon_phase == "new moon":
    print("witches night out!")
elif moon_phase == "half moon":
    print("thats a half moon")

# FIZZBUZZ EXAMPLE, order of operations for combined conditionals
# Check a number, if that number is divisible by 3, print "FIZZ"
# If that number is divisible by 5, print "BUZZ"
# if its divisible by 3 and 5 print "FIZZBUZZ"
number = 15
if number % 3 == 0 and number % 5 == 0:
    print("FIZZBUZZ")
elif number % 5 == 0:
    print("BUZZ")
elif number % 3 == 0 :
    print("FIZZ")

shirt = "One Piece Shirt"
pants = "blue"
coat = "red"

if shirt == "Drake Shirt":
    print("Cool, im wearing my drake shirt today!")
elif shirt == "The Weekend Shirt":
    print("ok i guess I'll wear my The Weekend Shirt")
elif shirt == "Blake Shelton":
    print("eww why do i have that shirt, i would never...")
else:
    print("Guess ill just wear this .·´¯`(>▂<)´¯`·. ")

# Potion Strength Check
potion_strength = 10
if potion_strength > 20:
    print("Its a super potent potion!")
elif potion_strength > 10:
    print("Its a moderately potent potion!")
else:
    print("This is some weak stuff")

# Checking Weather
weather = "rainy"
if weather == "sunny":
    print("Its a bright and sunny day! Hip hip hooray!")
elif weather == "rainy":
    print("carry your umbrella!")
elif weather == "snowy":
    print("do you want to build a snowman?!!?!")

# checking ranges of a player level
player_level = 12
if player_level < 5:
    print("You're not strong enough for this dungeon!")
# if player_level >= 5 and player_level < 10
elif 5 <= player_level < 10:
    print("You're at the perfect level for this dungeon")
elif player_level >= 10:
    print("Oh good! You can carry your friends through here!")

# simplified solution
if player_level < 5:
    print("You're not strong enough for this dungeon!")
# if player_level >= 5 and player_level < 10
elif player_level < 10:
    print("You're at the perfect level for this dungeon")
else:
    print("Oh good! You can carry your friends through here!")

# More else's and more dragons
is_dragon_present = True
has_treasure = False
#      truthy                  falsey
if is_dragon_present and not has_treasure:
    print("Enter with caution! Dragon ahead, but no treasure in sight! :(")
        #  falsey                 truthy
elif not is_dragon_present and has_treasure:
    print("No dragon here! Quick grab the loot!")
elif is_dragon_present and has_treasure:
    print("A mighty dragon guards hella lootz")
else:
    print("Theres no dragon or treasure, but feel free to explore anyway!")

"""
Instructions:

Traffic lights are universal symbols that guide drivers and pedestrians, ensuring safety on the roads. 
Each color of the traffic light conveys a specific instruction, from halting completely to proceeding with caution or moving ahead freely. 
Write a program that prompts the user to input the color of a traffic light (red, yellow, green) and outputs the action a driver should take.

light_color = "red"

output = "Stop"
output = "Scream yolo and accelerate through the light"
output = "Go"
"""

# light_color = "purple"
# if light_color == "red":
#     print("stop!")
# elif light_color == "yellow":
#     print("Scream yolo and accelerate through the light")
# elif light_color == "green":
#     print("go")
# else:
#     print("Thats not a valid light color")


# traffic_light = input("what color is the traffic light?")
# if traffic_light == "red":
#     print("stop")
# elif traffic_light == "green":
#     print("go")
# elif traffic_light == "yellow":
#     print("speed up and scream YOLO")

# light_color = input("What color is the light? ")
# if light_color == "red":
#     print("Please Stop!")
# elif light_color == "yellow":
#     print("Please slow down")
# elif light_color == "green":
#     print("Step on the gas!")
# else:
#     print("That light is broken it seems!")

# user_input = input("What color is the traffic light?")
# if user_input == "red":
#     print("red")
# elif user_input == "green":
#     print("green")
# elif user_input == "yellow":
#     print("yellow")

# driving = True
# while driving:
#     user_input = input("What color is the traffic light?")
#     if user_input == "red":
#         print("red")
#         driving = False
#     elif user_input == "green":
#         print("green")
#         break
#     elif user_input == "yellow":
#         print("yellow")
#         driving = False
#     else:
#         print("Please enter a valid light color!")

# light_color = input("What color is the traffic light?")
# if light_color == "red":
#     print("stop!")
# elif light_color == "yellow":
#     print("Scream yolo and accelerate through the light")
# elif light_color == "green":
#     print("go")
# else:
#     print("that is not a valid light color.")

# likes_sweet = input("Do you like your coffee sweet? (yes/no) ")
# likes_milk = input("Do you prefer milk in your coffee? (yes/no) ")

# if likes_sweet == "yes" and likes_milk == "yes":
#     print("How about a pumpkin spice latte?")
# elif likes_sweet == "no" and likes_milk == "yes":
#     print("An Americano with a dash of milk sounds good for you!")
# elif likes_sweet == "yes" and likes_milk == "no":
#     print("Try a black coffee with two sugars!")
# else:
#     print("Black coffee it is!")
    
# Nested Conditionals
# if this:
    #if this:
     #  if this:
        # do this
temperature = 14
if temperature < 25:
    print("It's a bit chilly")
    if temperature < 15:
        print("Ya know what, you should bring a heavy jacket!")

temperature = 4
if temperature < 25:
    print("It's a bit chilly")
    if temperature < 15:
        print("Ya know what, you should bring a heavy jacket!")
        if temperature < 5:
            print("ahhh man thats gonna freeze the mustache")

# Checking age restrictions
age = 17
if age >= 18:
    if age >= 21:
        print("You can drive, vote, and also enjoy an adult beverage!")
    else:
        print("You can drive and vote!")
else:
    print("You are too young to drive or vote :( Take the bus loser")

# Activity Planner
day = "Saturday"
time = "Evening"
clock_time = "11 am"
if day == "Saturday":
    if time == "Morning":
        print("Time for cartoons!")
        if clock_time == "10 am":
            print("Oh cool, its time for Pokemon. Gotta Catch Em All!")
        elif clock_time == "11 am":
            print("Believe in the heart of the cards, its time for yugioh!")
        else:
            print("I dont know whats on at that time....")      

    elif time == "Evening":
        print("Maybe a Movie Night?")
    else:
        print("Relax and Enjoy your Day!")
else:
    print("Be sad because its not Saturday. Even if its Sunday and still the\
           weekend you have to deal with the existential crisis of the impending Monday.")

# When do we do we indent?
# always going to indent after a colon
# and colon denotes a new block of code
# define function, start a conditional, start a loop
# def say_hello(): #after function definition
#     print("Function stuff goes here") 
# name = "Gimli"
# if name == "Gimli": # after conditional
#     print("I cannot make the jump, you have to toss me")
# while True: #after starting a loop
#     print("Do loopy stuff here!")
#     break
    

# Conditional Shorthand
# defining two variables in one line, using commas
x, y = 5, 10
if x > y:
    print("x is greater")
else:
    print("y is greater")


# expr1 if condition1 else expr2 if condition2 else expr
# result if condition is true
print("x is greater") if x > y else print("y is greater")
# adding an elif to a conditional shorthand
print("x is greater") if x > y else print("y is greater") if y > x else print("They're equal!")

name1 = "Tomato"
name2 = "Potato"
name3 = "Squash"
name4 = "Pumpkin"

print("The first name is ", name1) if name1 == "Ryan" else print("The second name is ", name2) if name2 == "Haya" else print("The third name is ", name3) if name3 == "Daniel" else print("The fourth name is ", name4)

# What to do depending on the weather!

weather = "rainy"
activity = "beach" if weather == "sunny" else "play super smash"
print(activity)

hour_of_day = 1
energy_level = 3

beverage = "coffee" if (6 <= hour_of_day < 12) and energy_level < 4 else "tea"
print(beverage)

import datetime
now = datetime.datetime.now()
print(type(now))
print(now)
string_time = str(now)
print(type(string_time))
print(string_time)
cool_time = string_time.split()
print(cool_time)
current_time = cool_time[1]
print(current_time)
now_time = current_time.split(':')
print(now_time)
now = now_time[0]
print(now)
now = int(now)
print(type(now))

beverage = "coffee" if (6 <= now < 12) and energy_level < 4 else "tea"
print(beverage)


"""
**Problem Statement**:
    You are developing a feature for a movie streaming platform that suggests a movie 
    genre to users based on their current mood and the day's weather. The platform has the following recommendation criteria:

    - If the user is feeling "happy" and the weather is "sunny", recommend a "Comedy".
    - If the user is feeling "happy" but the weather is not "sunny", recommend a "Romantic" movie.
    - If the user is feeling "sad", recommend a "Drama".
    - For any other mood, recommend an "Adventure" movie.

    Write a Python program that:

    1. Asks the user about their current mood (happy/sad/adventurous).
    2. Asks the user about the day's weather (sunny/rainy).
    3. Determines the movie genre based on the above criteria.
    4. Displays the recommended movie to the user.

    **Hint**:
    Use nested `if` statements to determine the movie genre based on the user's mood and the day's weather.
"""

# mood = input("What is your current mood? (happy/sad/adventurous)")
# weather = input("What is the weather like today? (sunny/rainy)")
# if mood == "happy":
#     if weather == "sunny":
#         print("You should watch a comedy!")
#     else:
#         print("You should watch a romantic movie!")
# elif mood == "sad": 
#     if weather == "sunny":
#         print("You should watch a drama!")
#     else:
#         print("You should watch a horror movie!")
# else:
#     print("You should watch an adventure movie!")



    
# user_mood = input("What is your current mood? (happy/sad/adventurous) ")
# current_weather = input ("What is today's weather? (sunny/rainy) ")

# if user_mood == "happy": 
#     if current_weather == "sunny":
#         movie = "Comedy"
#     elif current_weather != "sunny":
#         movie = "Romantic"
# elif user_mood == "sad":
#     movie = "Drama"
# else:
#     movie = "Adventure"

# print("You should watch a", movie, "movie")

    


# user_mood = input("How are you feeling today? (happy/sad/adventurous)")
# weather_today =input("what is the weather like today? (sunny/rainy)")
# if user_mood == "happy":
#     if weather_today =="sunny":
#         print("Watch a comedy movie")
#     else:
#         print("Watch a romantic movie")
# elif user_mood == "sad":
#     print("Watch a drama movie")
# else: 
#     print("Watch an adventure movie")



# print("\n")
# emotion = input("How are you feeling? ")
# weather = input("How's the weather where you are? ")
# if emotion == "happy":
#     if weather == "sunny":
#         print("Let's check out a comedy!")
#     elif weather == "rainy":
#         print("Grab the Hot coacoa, we're watching a Romantic movie")
# elif emotion == "sad":
#     print("Let's feel feelings with a Drama.")
# else:
#     print("Sounds like an adventure time! Let's watch an Adventure movie!")

# user_mood = input("What is your current mood? (happy, sad, adventurous) ")
# weather = input("How is the weather today? (sunny, rainy) ")
# if user_mood == "happy" and weather == "sunny":
#     print("You should watch Billy Madison!")
# elif user_mood == "happy" and not weather == "sunny":
#     print("You should watch a The Notebook")
# elif user_mood == "sad":
#     print("Watch 8 pounds!")
# else:
#     print("Watch Jurrasic Park!")

# user_mood = input("How are you feeling today? (happy/sad/adventurous) ")
# current_weather = input("How's the weather where you are? (sunny/rainy) ")
# output = ""
# if user_mood == "happy":
#     if current_weather == "sunny":
#         output = "I recommend a comedy. Have you seen 'What About Bob?'"
#     else:
#         output = "I recommend something romantic! 'Sleepless in Seattle' is a good one!"
# elif user_mood == "sad":
#     output = "You know what you gotta watch?? A drama! Time for 'Killers of the Flower Moon!'"
# else:
#     output = "Okay well, how about an adventure movie? 'Back to the Future' is one of my favorites!"
# print(output)


# mood = input("How are you feeling? : ")
# weather = input("How's the weather? : ")
# if mood == 'happy':
#     movie = "Comedy" if weather == 'sunny' else "Romantic Movie"
# else:
#     movie = "Drama" if mood == 'sad' else "Adventure"
# print(f"Hmm? Why not watch a {movie}?")




# mood = input("How are you feeling?")
# weather = input("How is today's weather?")
# if mood == "happy" and weather == "sunny":
#     print ("You should watch a comedic movie!")
# elif mood == "happy" and weather != "sunny":
#         print("You should watch a romantic movie!")    
# if mood == "sad":
#     print("You should watch a drama!")    
# else:
#     print("You should watch and adventure movie !")

# mood = input("What is your mood?")
# weather = input("What is the weather like?")
# # feeling = "happy"
# # weather = "sunny"
# if mood == "happy":
#     if weather == "cloudy":
#         print("Let's watch The Notebook")
#     elif weather == "sunny":
#         print("Let's watch The Hangover")
# elif mood == "sad":
#     if weather == "rainy":
#         print("Down in the dumps, let's watch The Pursuit of Happyness")
    

# else:
#     print("Action time! John Wick!")

# mood = input("How are you feeling today?")
# if mood != "happy":
#     print("Why dont you watch The Pursuit of Happiness ")
# else:
#     weather = input("What is the weather like today? ")
#     if weather == "sunny":
#         print("Watch Hot Rod!")
#     elif weather == "rainy":
#         print("Watch Lord of the Rings: The Two Towers")


# pass will let us skip after defining a function, creating a loop, creating a conditional, etc...

# pass with a conditional
if x > y:
    pass

# pass with function
def do_something():
    # i dont know what this function will do
    # num = 1 + 1
    # print(num)
    # print("i did something")
    pass   


# passing over an exception
try: 
    x = 1/0
except ZeroDivisionError:
    pass

print("The script goes on....")

# passing over loops
for i in range(5):
    # i dont know what to do with my i
    pass

value = 10

if value > 5:
    pass #ill implement something later
else:
    print("Value is not greater than 5")


