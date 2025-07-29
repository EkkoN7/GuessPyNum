import random


users_life = 5
user_select = input("In which range should the numbers be: 1 to ").strip()
user_select_isdigit = user_select.isdigit()
if user_select_isdigit == True:
    random_num = random.randint(1, int(user_select))
    print (random_num)
    while users_life > 0:
        user_guess = input("Guess a number: ")
        print(f"Users Life = {users_life}")
        if int(user_guess) == random_num:
            print("Congratulation! You won!")
        elif int(user_guess) > random_num:
            print("Too high")
            users_life -= 1
        elif int(user_guess) < random_num:
            print("Too low")
            users_life -= 1
    print("Game Over")


