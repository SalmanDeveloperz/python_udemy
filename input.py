# name= input("Enter your first name please: ")
# birth= input ("Enter Your birthdate (Day, Month) please: ")
#
# print(f"Hey {name}, thanks for letting us know, "
#       f"We'll wish you birthday at {birth}")


# Assignment

"""

String Assignment. (This can be tricky so feel free to watch solution so we can do it together)

- Ask the user how many days until their birthday

- Using the print()function. Print an approx. number of weeks until their birthday

- 1 week is = to 7 days.

"""

days_left= int(input("Kindly let us know how many days left until your birthday: "))

day_to_weeks= (days_left)/7

print(f"Approximately {round(day_to_weeks,2)} .number of weeks until your birthday")



