print("It's luch time and ya feelin' kind of hungry.")

print("Do you have any dietary restrictions?")
print("type 'yes' for yes and 'no' for no")
user_input = input()
if user_input == "yes":
    print("Are you vegetarian or gluten free?")
    print("type 'vegetarian' for vegetarian and 'gluten free' for gluten free")
    user_input = input()
    if user_input == "vegetarian":
        print("You go to a salad bar and enjoy crispiness of the lettuce!")
    elif user_input == "gluten free":
        print("Do you want pizza or pasta?")
        print("type 'pizza' for pizza and 'pasta' for pasta")
        user_input = input()
        if user_input == "pizza":
            print("Oh, no! The chef forgot to use a gluten free substitute!")
        elif user_input == "pasta":
            print("You enjoy your meal because you know there are worse options.")
        else:
            print("Sorry. There are not enough food options available. Go home.")
    else:
        print("Sorry. There are not enough restaurants available. Go home.")

elif user_input == "no":
    print("Do you want to eat a healthy or unhealthy meal?")
    print("type 'healthy' for healthy and 'unhealthy' for unhealthy")
    user_input = input()
    if user_input == "healthy":
        print("Would you prefer an expensive or cheap meal?")
        print("type 'expensive' for expensive and 'cheap' for cheap")
        user_input = input()
        if user_input == "expensive":
            print("You go to Whole Foods and have a yummy meal.")
        elif user_input == "cheap":
            print("You go to Subway and enjoy your sandwich.")
        else:
            print("Sorry. Other locations are out of your budget.")
    elif user_input == "unhealthy":
        print("Would you rather go to McDonald's or Burger King?")
        print("type 'McDonald's' for McDonald's and 'Burger King' for Burger King")
        user_input = input()
        if user_input == "Burger King":
            print("You enjoy your lovely meal.")
        elif user_input == "McDonald's":
            print("You get a Happy Meal.")
            print("Sorry. You have food poisoning.")
        else:
            print("Sorry. There is too much traffic to go to other locations.")

else:
    print("Sorry. There are no available restaurants. Go home.")
