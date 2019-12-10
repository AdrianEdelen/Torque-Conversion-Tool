def numberGuessingGame():
    import random
    while True:

        def numberGuess():
            while True:
                try:
                    numberGuess = int(
                        input("Guess a number between 1 and 20!: "))
                except ValueError:
                    print(
                        "That is not a number that is 1 through 20, try again."
                    )
                    continue
                if numberGuess < 1 or numberGuess > 20:
                    print(
                        "That is not a number that is 1 through 20, try again."
                    )
                    continue
                else:
                    break

        numberGuess()
        randomGen = random.randint(1, 20)
        print(randomGen)
        exit = input(
            "Press R and hit enter to return to main menu or just press any key and enter to play again.... \n: "
        )
        if exit == "r" or exit == "R":
            break
        else:
            continue

