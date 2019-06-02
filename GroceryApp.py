def shopping():
    print("Let's go shopping. What would you like to search for first?")
    answer = input()

    print("Here are the prices for " + answer)



print("Would you like to go shopping today?")

answer = input() 

if answer == "yes":
    print("What should we get?")
    list1 = input() 
    print("Great! We are going to get " + list1)
    shopping()
    




if answer == "no":
    print("Maybe tomorrow")
