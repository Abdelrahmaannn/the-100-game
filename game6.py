while True:
    print("Welcome To THE 100 GAME ")
    print('MENU')
    print('1 - Start multiplayer game')
    print('2 - Quit game')
    choice = int(input('What are you going to do? Enter the number representing your choice:'))
    if choice == 1:
        print('lets Have Fun :) ')
    elif choice == 2:
        print('See you soon Good Bye :(')
        break  # Here the program stops and quit
    else:
        print("Welcome To THE 100 GAME ")
        print(' MENU ')
        print('1 - Start multiplayer game')
        print('2 - Quit game')
        choice = int(input('What are you going to do? Enter the number representing your choice.'))
        if choice == 1:
            print('lets Have Fun :) ')
        elif choice == 2:
            print('See you soon Good Bye :(')
            break  # Here the program stops and quit
        else:
            print('Awesome! Type again.')
    while True:
        print('Player 1 Name:')
        oneName = input()
        print('Player 2 Name:')
        twoName = input()
        print('Welcome, ' + oneName + ' and ' + twoName + ', to 100!')
        print('You will each take turns to choose a number between 1 and 10.')
        print('The first person to reach 100 is the winner.')
        print("Have fun, and lets Goooo!")
        totalNumber = 0
        turn = False
        while totalNumber < 100:
            numberOne = input(
             oneName + ', Enter a number between 1 and 10.')
            numberOne = int(numberOne)
            totalNumber += numberOne
            print("Got it, " + oneName + "! Below is the total right now:")
            print(totalNumber)
            turn = False
            if totalNumber > 100:
               break
            numberTwo = input(
                twoName + ', Enter a number between 1 and 10.')
            numberTwo = int(numberTwo)
            totalNumber += numberTwo
            print("Got it, " + twoName + "! Below is the total right now:")
            print(totalNumber)
            turn = True
        if turn == True:
            print(twoName + " Wins!! congratulations , Good Bye :) ")
        else:
            print(oneName + " Wins!! congratulations , Good Bye :) ")