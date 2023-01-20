print ('please think of a number between 0 and 100!')
low = 0 
high = 100 
med = (high + low ) // 2
state = True 
while state :
    print ('is your secret number ' + str(med))
    guess = input ("enter 'h' to indicate the guess is too high . enter 'l' to indicate the guess is too low . enter 'c' to indicate the guess is correct : ")
    if guess == 'c' :
        print ('game over . your secret number was : ' + str(med))
        state = False 
    elif guess == 'h' :
         high = med
         med = (high + low)//2
    elif guess == 'l' :
        low = med 
        med = (high +low) //2
    else :
        print ('sorry , i did not understand your input!!')
