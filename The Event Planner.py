# Task 1: Code Correction
 
attendees = int(input("Enter number of attendees: "))
 
venue = "large hall" if attendees > 100 else "conference room"
 
print(venue)
 
 
# Task 2: Venue Selection
 
attendees = int(input("Enter number of attendees: "))
 
venue = "Large Hall" if attendees > 100 else "Conference Room"
 
av_recommendation = "audio system" if attendees > 100 else "projector"
 
print(f"We recommend booking the {venue} with the {av_recommendation}!")
 
 
# Task 3: Catering Choices
 
vegetarian = input("Would you like vegetarian food? (yes or no) ")
 
caterer = print("I recommend Veggie Delight Caterers!") if vegetarian == "yes" else print("I recommend Gourmet Meals Caterers!")