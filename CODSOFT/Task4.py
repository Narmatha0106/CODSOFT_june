#rock-paper-scissors
import random
choices=["rock","paper","scissors"]
user_score=0
computer_score=0
while True:
    print("\n~~~~~~ROCK PAPER SCISSORS~~~~~~~~")
    user=input("Enter rock,paper,scissors:").lower()
    if user not in choices:
        print("Invalid input")
        continue
    computer=random.choice(choices)
    print("Computer Choice:",computer)
    if user==computer:
        print("It's a Tie!")
    elif(user=="rock"and computer=="scissors")or(user=="paper"and computer=="rock")or(user=="scissors"and computer=="paper"):
        print("You Win!")
        user_score+=1
    else:
        print("Computer Wins!")
        computer_score+=1
    print(f"Score->You:{user_score}|Computer:{computer_score}")
    play=input("Play Again?(yes/no): ")
    if play.lower()!="yes":
        break