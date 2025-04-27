# String Formatting

# first_name = "Mahfuz"
# print(f"Hi {first_name}")
# sentence = "Hi This is {} {}"
# last_name = "Rahman"
# print(sentence.format(first_name,last_name))

#User Input
first_name = input("Enter Your Name: ")
age = input("How old are you? ")
print(f"Hi {first_name}, You are {age} years old")

first_name = input("Enter Your Name: ")
days_until_bd = input("How Many Days Until Your Birthday? ")
weeks_remaining = int(int(days_until_bd)/7)
remaining_days = int(days_until_bd)%7
print(f"Hi {first_name}, You have {weeks_remaining} Weeks and {remaining_days} Days before your birthday. Happy Birthday")
