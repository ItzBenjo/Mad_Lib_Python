#This is the Introduction, it will appear at the beginning 
introduction = input("Hello! Welcome to the Outside Adventures and Much Much More Game presented by BSF and Sons! This game is kids friendly: ages 4 to 12, and educational. It is also environmentally friendly: action and adventure with things found outside, completely out of recycled materials, and 35% of what you pay goes to an environmental foundation. You can also socialize:  add as many players as you want and play with your friends.")
print(introduction)
#first_sentence is the is the second introduction
first_sentence = input("Hello there! Welcome To Outside Adventures and Much Much More Game.")
print(first_sentence)
#first_question is the nice introduction question
first_question = input("How are you doing? ")
print(first_question)
# if else satement to get an answer to the user's answer
if first_question == "good"or"Good":
    print("I feel Good too")
elif first_question == "bad"or"Bad":
    print("Sorry for you")
elif first_question == "great"or"Great":
    print("Awseome me too")
else:
    print("Ok")
#We are going to explain the rules
rules = input("The rules are simple, each level, you will have a different thing to do. The fist level cannot be failed, like that you do not fail the game. In each level you will have questions, that have a multiple choice option. If your answer is incorrect you will have a second chance. If it is incorrect again, you have failed the level, so you will need to go back to the previous level. You will have a different question than the one that was asked. To win the game, you will need to complete every level. Good luck!")
print(rules)
#level_one_intro is a welcoming intro
level_one_intro = input("Welcome to Level One!")
print(level_one_intro)
#asking a question that will explain level one
level_one_second_intro = input("What are we going to do in the first level?")
print(level_one_second_intro)
#Now we are explaining level one
level_one_second_mini_intro = input("In the first level we are going to do a simple Mad Lib.")
print(level_one_second_mini_intro)
#This is a level one
level_one = input("Take a (noun) and other things found in your (noun) and (verb) them against a tree. Then cover the (noun) with leaves maybe even use a tarp. Now you have your own (noun). We dare you to sleep in your creation for one night. Make sure to bring marshmallows! When you wake up you must be hungry from your night in your (noun). Go back into your house and make a (noun) salad, squeezed fresh ( noun) to make juice. Put your wheat bread in your (noun), and enjoy it with (noun). Bon appetit!")
print(level_one)
#This is the first sentence of the first level
#Take a (noun) and other things found in your (noun) and (verb) them against a tree.
#nouna1 is the fisrt noun of the first sentence
nouna1 = input("Please enter a first noun that will go well with the first sentence: ")
#printing the answer of the user and adding some positive things to it!
print(nouna1 + ", that is one of my favorite nouns!")
#nouna2 is the second noun of the first sentence
nouna2 = input("Please enter a second noun that will go well with the fisrt sentence: ")
#printing the answer of the user and adding some positive things to it!
print(nouna2 + ", good choice!")
#verba1 is the first verb of the first sentence
verba1 = input("Please enter the fisrt verb of the first sentence: ")
#printing the answer of the user and adding some positive things to it!
print(verba1 + ", wow, you know that verb! I am really impressed, I under estimated you.")
#Now we are showing to the user only th first sentence with the noun and verbs he entered
print("Take a " + nouna1 + " and other things found in your " + nouna2 + " and " + verba1 + " them against a tree.")
#This is the second sentence of the first level
#Then cover the (noun) with leaves maybe even use a tarp. Now you have your own (noun).
#nounb is the noun for the second sentence
nounb = input("Please enter a noun for the second sentence: ")
#printing the answer of the user and adding some positive things to it!
print(nounb + ", that is a perfect noun for the sentence!")
#Now we are showing to the user only the second sentence with the noun he entered
print("Then cover the " + nounb + " with leaves maybe even use a tarp.")
#This is the third sentence of the first level
#We dare you to sleep in your creation for one night. Make sure to bring marshmallows! When you wake up you must be hungry from your night in your (noun). 
#nounc is the noun only for the third sentence
nounc = input("Please enter a noun for the third sentence: ")
#printing the answer of the user and adding some positive things to it!
print(nounc + ", I honestly think you should skip a grade, how do you know that noun, are you a genius. I am really impressed!!")
#Now we are printing the third sentence with the noun the user entered for the third answer
print("Now you have your own" + nounc + ".")
#nound is the noun for the fourth sentence
nound = input("Please enter a noun for the fourth sentence: ")
#printing the answer of the user and adding some positive things to it!
print(nound + ", I was thinking about the same noun, that's a great one!")
#printing the fourth sentence with the noun the user entered
print("We dare you to sleep in your creation for one night. Make sure to bring marshmallows! When you wake up you must be hungry from your night in your" + nound + ".")
#Go back into your house and make a (noun) salad, squeezed fresh (noun) to make juice.
#noune is the first noun for the fith sentence
noune = input("Please enter a first noun for the fith sentence: ")
#printing the answer of the user and adding some positive things to it!
noune("How did you guess " + noune + " is my moms favorite noun")
#noun2e is the first noun for the fith sentence
noun2e = input("Please enter a second noun for the fith sentence: ")
#printing the answer of the user and adding some positive things to it!
print(noun2e + ", good choice!")
#Now we are printing the fith sentence with the two nouns the user entered for the fith answer
print("Go back into your house and make a " + noune + " salad, squeezed fresh " + noun2e + " to make juice.")
#Put your wheat bread in your (noun), and enjoy it with (noun). Bon appetit!
#nounf is the first noun for the sixth sentence
nounf = input("Please enter a first noun for the sixth question: ")
#printing the answer of the user and adding some positive things to it!
print(nounf + ", I like that one!")
#noun2f is the second noun for the sixth sentence
noun2f = input("Please enter a second noun for the sixth question: ")
#printing the answer of the user and adding some positive things to it!
print(noun2f + ", nice ending I like it")
#Now we are printing sixth sentence with the two nouns the user entered for the sith answer
print("Put your wheat bread in your " + nounf + ", and enjoy it with " + noun2f + ". Bon appetit!")
#Now we are telling the user that we are showing the whole Mad Lib to the user
print("Here is the Mad Lib that you did: ")
#Now we are printing the mad lib for the user to see
print("Take a " + nouna1 + " and other things found in your" + nouna2 + " and " + verba1 + " them against a tree. Then cover the " + nounb + " with leaves maybe even use a tarp. Now you have your own " + nounc + ". We dare you to sleep in your creation for one night. Make sure to bring marshmallows! When you wake up you must be hungry from your night in your " + nound + ". Go back into your house and make a " + noune + " salad, squeezed fresh " + noun2e + " to make juice. Put your wheat bread in your " + nounf + ", and enjoy it with " + noun2f +". Bon appetit!")
print("You completed the level one!")
print("Mazel Tov!")








