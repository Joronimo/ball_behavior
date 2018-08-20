from time import sleep

def print_holes():
    print("""
|         | |         |
|_________| |_________|
   HOLE A      HOLE B
""")

def intructions1():
    print("In this game you have a ball.") 
    sleep(1.5)
    print("There are two holes side by side.") 
    print("Hole A and Hole B.") 
    sleep(1)
    print("You can place the ball in either hole.") 
    print("Put the ball in hole B.") 
    sleep(1.5)
    
    print("When prompted to select a hole to drop the ball in.")
    sleep(1.5)
    print_holes()


def chose_B(): 
    chose_B = input("Choose a hole: HOLE A or HOLE B.")

    while True:
        if chose_B == "HOLE B":
            print("Good choice!")
            print("""
               +++++
|         | | +++++++ |
|_________| |__+++++__|
   HOLE A      HOLE B
""")
            break
        else:
            chose_B = input("Wrong input. Are you sure you're paying attention? Try one more time.")

def option_selection(has_played):
    print_holes()
    option_selection = input("Hole B or Hole A:").upper()
    option_store = "option_store.txt"
    has_played_result = "has_played.txt"

    while True:
        if option_selection == "HOLE A":
            print("""
   +++++    
| +++++++ | |         |
|__+++++__| |_________|
   HOLE A      HOLE B
""")
            result = "HOLE A"
            break
        elif option_selection == "HOLE B":
            print("""
               +++++
|         | | +++++++ |
|_________| |__+++++__|
   HOLE A      HOLE B
""")
            result = "HOLE B"
            break
        else:
            option_selection = input("terible, try again. Hole A or Hole B.").upper()
    
    if has_played != "Y":
        print(result, file=open(option_store, "a"))
    else:
        print(result, file=open(has_played_result, "a"))




print("Welcome to the ball game. This is not a ballgame, but rather a game involving a ball.")
sleep(1.5)

while True:
    has_played = input("have you played this game before? Y or N").upper()
    if has_played == "Y" or has_played == "N":
        print("")
        break
    else:
        print("please use y or n")
        print("")
        
 
intructions1()

chose_B()

print("You've chosen the right hole.")
sleep(1)
print("")
print("Now given your options and free will, which hole would you like to drop the ball into?")

option_selection(has_played)

def count_chosen(doc_options):
    f = open(doc_options, 'r')
    x = f.readlines()
    f.close()

    total = len(x)
    totalB = x.count("HOLE B\n")
    totalA = total - totalB

    return total, totalB, totalA


if has_played == "Y":
    a, b, c = count_chosen("option_stored.txt")
    print("Of the {} people who played for the game the first time, {} chose B and {} chose A".format(a, b, c))
elif has_played == "N":
    a, b, c = count_chosen("has_played.txt")
    print("Of the {} people who haved played the game before, {} chose B and {} chose A".format(a, b, c))

# B_count = 0

# for B in x:
#     if B == "HOLE B\n":
#         B_count = B_count + 1

##option_selection():
##prompt user



# A = 6 + 1

# read it and then overwrite and save it
# w3schools/python_file_handling.asp