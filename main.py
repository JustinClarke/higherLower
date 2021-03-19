import art
from game_data import data
import random

score = 0
game_over = False

def compare(follow1, follow2, users_ans):
    global score, game_over
    if follow1 > follow2 and users_ans == 'A':
        print("You have chosen correctly!")
        score += 1
    elif users_ans == 'A':
        print(f"Wrong answer. Final Score = {score}")
        game_over = True
    
    if follow1 < follow2 and users_ans == 'B':
        print("You have chosen correctly!")
        score += 1
    elif users_ans == 'B':
        print(f"Wrong answer. Final Score = {score}")
        game_over = True

def display():
    firstpair = random.choice(list(data))
    secondpair = random.choice(list(data))

    name = firstpair.get("name")
    description = firstpair.get("description")
    country = firstpair.get("country")

    othername = secondpair.get("name")
    otherdescription = secondpair.get("description")
    othercountry = secondpair.get("country")
    
    print(art.logo)
    print(f"Compare A: {name}, a {description}, from {country}.")
    print(art.vs)
    print(f"Compare B: {othername}, a {otherdescription}, from {othercountry}.")
    print(firstpair.get("follower_count"),secondpair.get("follower_count"))
    users_answer = input("Who has more followers? Type 'A' or 'B': ")
    compare(firstpair.get("follower_count"),secondpair.get("follower_count"), users_answer)

while not game_over:
    display()