print("Welcome to the Savings Calculator. We will help you track your savings for the month!")
earnings = input("How much money do you earn a month?")
    

food = input("How much money do you spend on food in a month?")
clothing = input("How much money do you spend on clothing in a month?")
transportation = input("How much money do you spend on transportation in a month?")
social_activities = input("How much money do you spend on social_activities in a month?")

def operation(earnings,food,clothing,transportation,social_activities):
    remaining = int(earnings)-int(food)-int(clothing) -int(transportation) -int(social_activities)
    if remaining < 0:
        print("You suck!You're at a " + str(remaining) + " deficit" )
        
    elif remaining > 0: 
        print("Congratulations! You still have " + "$" + str(remaining) + " to spend")


    elif remaining == 0:
        print("You have no money left!")

operation(earnings, food, clothing, transportation, social_activities)



# print(operation(earnings, food,clothing,transportation,social_activities))

# operation(earnings, food,clothing,transportation,social_activities) = total 
