""" String Formatting """

# first_name = "Mahfuz"
# print(f"Hi {first_name}")
# sentence = "Hi This is {} {}"
# last_name = "Rahman"
# print(sentence.format(first_name,last_name))

"""User Input"""
# first_name = input("Enter Your Name: ")
# age = input("How old are you? ")
# print(f"Hi {first_name}, You are {age} years old")

# first_name = input("Enter Your Name: ")
# days_until_bd = input("How Many Days Until Your Birthday? ")
# weeks_remaining = int(int(days_until_bd)/7)
# remaining_days = int(days_until_bd)%7
# print(f"Hi {first_name}, You have {weeks_remaining} Weeks and {remaining_days} Days before your birthday. Happy Birthday")

""" List Type """

# my_list = [45,87,12,37,92,33]
# print(my_list)
# print(my_list[2])
# my_list[0] = 41
# print(my_list[-2:-1])
# my_list.append(100)
# my_list.insert(2,50)
# my_list.remove(92)
# my_list.pop(-1)
# my_list.sort(reverse=True)
# print(my_list)

""" Sets and Tuples """
# my_sets = {1,2,3,4,5,1,2}
# print(my_sets)
# my_sets.add(6)
# print(my_sets)
# my_sets.update([6,7])
# print(my_sets)
# my_sets.remove(5)
# print(my_sets)
# my_sets.discard(2)
# print(my_sets)
# print("+++++++++++++++++++++++++++")
# my_tuples = (1,2,3,4,5,1,2)
# print(my_tuples.count(5))

""" Dictionaries """
my_dict = {
    "name" : "mahfuz",
    "age" : 23,
    "ID" : 1138 
}
print(my_dict)
print(my_dict.get('age'))
my_dict.pop('ID')
print(my_dict)
my_dict["section"] = "31B1"
print(my_dict.items())
my_dict2 = my_dict.copy()
my_dict2.pop('age')
print(my_dict2, my_dict)

for x,y in my_dict.items():
    print(x + "-" + str(y))