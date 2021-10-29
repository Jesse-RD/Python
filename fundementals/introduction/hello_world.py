#1 - Print "Hello World"
print("Hello World")

#2 - Print "Hello Noelle!" witht the name in the variable
name = "Noelle"
print("Hello", name, "!")
print("Hello " + name + "!")

#3 - Print "Hello 42!" with the number in the variable
name = 42
print("Hello", name,"!")
print("Hello " + str(name) + "!") #resolved error with str(name)

#4 - Print "I love to eat sushi and pizza." with the foods in the variables
fave_food1 = "sushi"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with and f-string