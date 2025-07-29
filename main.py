import random

ascii_art = r'''
   ____                       ____          _   _                 
  / ___|_   _  ___  ___ ___  |  _ \ _   _  | \ | |_   _ _ __ ___  
 | |  _| | | |/ _ \/ __/ __| | |_) | | | | |  \| | | | | '_ ` _ \ 
 | |_| | |_| |  __/\__ \__ \ |  __/| |_| | | |\  | |_| | | | | | |
  \____|\__,_|\___||___/___/ |_|    \__, | |_| \_|\__,_|_| |_| |_|
                                    |___/                         
'''

acsii_win = r'''
    .-'"'-.
   / #     \
  : #       :  .-'"'-.
   \       /  / #     \
    \     /  : #       :
jgs  `'q'`    \       /
       (       \     /
        )       `'p'`
       (          )
        )        (
                  )
'''

print(ascii_art)


user_select = input("Welcome to GuessPyName! In which range should the numbers be (e.g., 1 to max. 9000)?\nUser: 1 to ").strip()
users_life = input("How many guesses do you get (max: 100)?\nUser: ").strip()
users_life_isdigit = users_life.isdigit()
user_select_isdigit = user_select.isdigit()
if user_select_isdigit == True and users_life_isdigit == True:
    if int(users_life) <= 100 and int(user_select) <= 9000:
        users_life_int = int(users_life)
        random_num = random.randint(1, int(user_select))
        is_running = True
        while users_life_int > 0 and is_running == True:
            print(f"Users Life = {users_life_int}")
            user_guess = input("Guess a number: ")
            user_guess_isdigit = user_guess.isdigit()
            if user_guess_isdigit == True:
                if int(user_guess) == random_num:
                    print(acsii_win)
                    print("Congratulations! You won!")
                    is_running = False
                elif int(user_guess) > random_num:
                    print("Too high")
                    users_life_int -= 1
                elif int(user_guess) < random_num:
                    print("Too low")
                    users_life_int -= 1
            else:
                print("Enter a number.")
        if users_life_int == 0:
            print("Game Over")
    else:
        print(f"Please enter only valid numbers. You entered \'{user_select}\' for the range and \'{users_life}\' for the number of guesses.")
else:
    print(f"Please enter only numbers. You entered \'{user_select}\' for the range and \'{users_life}\' for the number of guesses.")