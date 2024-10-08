# Task 1: Code Correction
 
place = input("Choose a place: forest or cave? ")
 
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else:
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
 
 
# Task 2: Setting the Scene
 
place = input("Choose a place: forest or cave? ")
 
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    light = input("Would you like to light a torch or proceed in the dark? ")
    if light == "light a torch":
      print("A light is helpful to guide your way to find the hidden treasure!")
    elif light == "proceed in the dark" :
      print("Go with caution on your quest to find the hidden treasure!")
 
 
# # Task 3: Default Path
 
place = input("Choose a place: forest or cave? ")
 
if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
      print("You found a bird's nest!")
    elif action == "cross a river":
      print("You found a boat!")
    else:
      pass
elif place == "cave":
    light = input("Would you like to light a torch or proceed in the dark? ")
    if light == "light a torch":
      print("A light is helpful to guide your way to find the hidden treasure!")
    elif light == "proceed in the dark":
      print("Proceed with caution on your quest to find the hidden treasure!")
    else:
      pass
else:
  pass