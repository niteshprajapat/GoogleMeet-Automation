import bot

print("1. Signup")
print("2. Start Meeting")
print("3. Exit")

user_choice = int(input("Enter your Choice good friend!! "))


if __name__ == '__main__':
    if user_choice == 1:
        bot.sign_in()

    elif user_choice == 2:
        bot.LETS_START_MEETING()

    elif user_choice == 3:
        quit()

    else:
        pass
    
    