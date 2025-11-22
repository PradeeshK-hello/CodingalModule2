list = [80, 83, 86, 374, 371, 163, 159, 372, 965, 110]

list.sort()
print(list)

guess = int(input("Enter your guess:"))

if guess in list:
    if guess < list[6]:
        print("I'M SORRY, YOUR GUESS WAS INCORRECT. THE NUMBER IS HIGHER.")
    elif guess > list[6]:
        print("I'M SORRY, YOUR GUESS WAS INCORRECT. THE NUMBER IS LOWER.")
    else:
        print("CORRECT! IT INDEED WAS 371!")
else:
    print("INVALID GUESS. PLEASE ENTER A NUMBER IN", list)