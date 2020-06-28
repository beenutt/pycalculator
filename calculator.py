name = str(input("Greetings user, what is thou name?"))
#Takes the users name!
emotion = str(input("That is great "+str(name)+", How are you doing?"))
#Asks how they are doing
num1 = float(input("That is great! Please enter the first number you want calculated! For subtraction, please enter the minuend and for division enter the original number before division."))
#Takes the first number
num2 = float(input("Thanks! Please enter the second number you want calculated! For subtraction, ender the subtrahend and for division enter the number you want the first number to be divided by."))
#Takes the second number
choice = str(input("Perfect! Do you want these numbers to be added together, multiplied or divided? Maybe subtraction? A for addition, M for multiplication, D for division, S for subtraction."))
#Asks if they want division, addition, subtraction or multiplication.
if choice == "A":
    answer = num1 + num2
    print("The answer is "+str(answer)+"!")
#Addition method
elif choice == "M":
    answer2 = num1 * num2
    print("The answer is "+str(answer2)+"!")
#Multiplication method
elif choice == "D":
    answer3 = num1 / num2
    print("The answer is "+str(answer3)+"!")
#Division method
elif choice == "S":
    answer4 = num1 - num2
    print("The answer is "+str(answer4)+"!") 
#Subtraction method
else: 
    print("That is not valid! Please restart the program!")
#Denies any random letters or numbers


# By Mosesiah