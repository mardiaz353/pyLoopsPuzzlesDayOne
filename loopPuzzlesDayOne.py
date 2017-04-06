
#Challenge 3 My Favorite Ingredients:
#Create a list that contains the five different
#ingredients (given) and create a loop that prints
#out the list with numbers like this:
# 1 snails
# 2 leeches
# 3 gorilla belly button lint
# 4 caterpillar eyebrows
# 5 centipede toes
x = 1

ingredients = [" ", "snails", "leeches", "gorilla belly - button lint",
               "catepillar eyebrows", "centipede toes"]
while x < 6:
    print(x, ingredients[x])
    x = x + 1

#Challenge 2 Even numbers:
#Create a loop that prints even numbers until it reaches
#your age and will look like this
# 2
# 4
# 6
# 8
# 10
# 12
# 14

age = 0

while age < 29:
    print(age)
    age = age + 2

#If we were solving this for someone with an odd numbered age
#the code would look like this

age = 1

while age < 30:
    print(age)
    age = age + 2

#Here I counted 0 as an even number. Not sure what the math
#gods will think of that though.

#Challenge 4: Your Weight on the Moon
#If you were standing on the moon right now, your weight would be 16.5
#percent of what it is on Earth.
#You can calculate that by multiplying your Earth weight by 0.165.
#If you gained a kilo in weight every year for the next 15 years,
#what would your weight be when you visited the moon each year
#and at the end of the 15 years? Write a program using a for loop that
#prints your moon weight for each year.
#This one included no sample output.

earthWeightVar = 0.165

#my earth weight is 120 lbs
#120 x 0.165 = 19.8 kilos
myMoonWeight = 19.8

for x in range(1, 16):
    
    print(myMoonWeight)
    myMoonWeight = myMoonWeight + 1
