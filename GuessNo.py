import random

randomNo=random.randint(1,9)



guess1= int(input("Enter a Number-"))

if guess1>randomNo :
    print("Your Guess was a bit High")
   

if guess1<randomNo :
    print("Your Guess was a bit Low")
    
    
if guess1==randomNo :
    print("Your Guessed it write")


if guess1!=randomNo :  
    guess2= int(input("Enter a Number-"))

    if guess2>randomNo :
        print("Your Guess was a bit High")
   

    if guess2<randomNo :
        print("Your Guess was a bit Low")
    
    
    if guess2==randomNo :
        print("Your Guessed it write")

    elif guess2!=randomNo :  
        guess3= int(input("Enter a Number-"))

        if guess3>randomNo :
            print("Your Guess was a bit High")
   

        if guess3<randomNo :
            print("Your Guess was a bit Low")
    
    
        if guess3==randomNo :
            print("Your Guessed it write")

        elif guess3!=randomNo :  
            guess4= int(input("Enter a Number-"))

            if guess4>randomNo :
                print("Your Guess was a bit High")
   

            if guess4<randomNo :
                print("Your Guess was a bit Low")
    
    
            if guess4==randomNo :
                print("Your Guessed it write")


            elif guess4!=randomNo :  
                guess5= int(input("Enter a Number-"))

                if guess5>randomNo :
                    print("Your Guess was a bit High")
   

                if guess5<randomNo :
                    print("Your Guess was a bit Low")
    
    
                if guess5==randomNo :
                    print("Your Guessed it write")

else:print("You Missed It")
   

