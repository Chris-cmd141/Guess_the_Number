import random
sec_num = random.randint(1,20)
def guessing_game():
    
    while True:
        guess = int(input("guess a whole number between 1 and 20 "))
        if guess < 1 or guess > 20:
            print("out of range")   
        elif guess > sec_num:
            print("it is to high, try again")
        elif guess < sec_num:
            print("it is too low, try again")
        else:
            print(f"Bravo, you picked the correct number {sec_num}!")
            break
guessing_game()    
