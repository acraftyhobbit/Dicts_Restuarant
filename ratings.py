"""Restaurant rating lister."""
#def get_user_score():
   #user_input_score = raw_input("What score would you give that restaurant?\n")
   #return user_input_score


with open('scores.txt') as scores_file:
    restaurant_ratings = {}
    user_choice = raw_input("What would you like to do?\n"
                            "Pick 1 for to see all rating.\n"
                            "Pick 2 to add a new restaurant rating.\n"
                            "Enter q to quite")
    if user_choice == "2":
        user_input_restuarant = raw_input("What restaurant would you like to rate?\n")
        #user_input_score = raw_input("What score would you give that restaurant?")
        #get_user_score()
        while True:
            try:
                user_input_score = int(raw_input("Please enter a rating:\n"))

            except ValueError:
                print "Please enter a score between 1 and 5"

            else:
                if user_input_score > 5 or user_input_score < 1:
                   print "Please enter a score between 1 and 5"
                else:
                    break


        restaurant_ratings[user_input_restuarant] = user_input_score
    elif user_choice == "1":   

        for row in scores_file:
            restaurant_name, rating = row.split(":")
            restaurant_ratings[restaurant_name] = rating.strip()
        
        sorted_restaurants = sorted(restaurant_ratings.items())

        for restaurant, score in sorted_restaurants:
            print "{} is rated at {}.".format(restaurant, score)
    elif user_choice == "q":
            exit()

