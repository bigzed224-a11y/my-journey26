# Create a kyc app that collects info from users
# Info includes: Name, surname, age, State of origin, occupation, tribe.

name = input("enter your first name: ")
lastname = input("enter your last name: ")
age = input("enter your age:")
gender = input("are you male or female?:")
state = input("enter your state of origin: ")
occupation = input("what is your occupation?: ")
tribe = input("what nigeria tribe are you from?: ")

# print("customer profile:\t")
# print("\tFull name -",name,lastname)
# print("\tAge -",age)
# print("\tgender -",gender)
# print("\tstate of origin -",state)
# print("\t occupation -",occupation)
# print("\tTribe -",tribe)
print(f"""customer profile:\n\t
          -> Full Name: {name} {lastname}\t
          -> age: {age}\t
          -> gender: {gender}\t
          -> Occupation: {occupation}\t
          -> tribe : {tribe}
""")