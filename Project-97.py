def numberguessingGame():
    chances=5
    number=3
    numberGuessing=input("Guess a Number (between 1-9)")
    while chances < 5:
        if numberGuessing == number:
            print("Congratulation You Won")
            break
    if not chances < 5:
            print("You Lose! The Number is",number)
numberguessingGame()        