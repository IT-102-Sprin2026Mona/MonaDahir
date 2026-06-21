''''
Create a loop and condition that takes a input and if its a 
yes print it 10 times when return a reply
'''       

#This is going to take an input from the user
answer = input("Is today a good day? (y/n) ").lower()


#Its an if statement checking if the string is equal to y and if so print yes it is
if answer == "y":
    for x in range(10):
        print("Yes it is")
elif answer == "n":
    print("Im sorry")
else: 
    print("Please try again")


