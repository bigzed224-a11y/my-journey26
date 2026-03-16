# Create a kyc app that collects info from users
# Info includes: Name, surname, age, State of origin, occupation, tribe.

# name = input("enter your first name: ")
# lastname = input("enter your last name: ")
# age = input("enter your age:")
# gender = input("are you male or female?:")
# state = input("enter your state of origin: ")
# occupation = input("what is your occupation?: ")
# tribe = input("what nigeria tribe are you from?: ")

# print("customer profile:\t")
# print("\tFull name -",name,lastname)
# print("\tAge -",age)
# print("\tgender -",gender)
# print("\tstate of origin -",state)
# print("\t occupation -",occupation)
# print("\tTribe -",tribe)
# print(f"""customer profile:\n\t
#           -> Full Name: {name} {lastname}\t
#           -> age: {age}\t
#           -> gender: {gender}\t
#           -> Occupation: {occupation}\t
#           -> tribe : {tribe}
# """)



def get_valid_input(prompt, validation_type):
    while True:
        user_input = input(prompt).strip()
        
        if validation_type == "alpha":
            if user_input.isalpha():
                return user_input.capitalize()
            print("Invalid input: Please use letters only.")
            
        elif validation_type == "digit":
            if user_input.isdigit() and int(user_input) > 0:
                return user_input
            print("Invalid input: Please enter a valid positive number.")

# --- Main Program ---
print("--- Customer Profile Setup ---")

first_name = get_valid_input("Enter First Name: ", "alpha")
last_name  = get_valid_input("Enter Last Name: ", "alpha")
age        = get_valid_input("Enter Age: ", "digit")
gender = get_valid_input("are you male or female?:", "alpha")
state = get_valid_input("enter your state of origin:", "alpha")
occupation = get_valid_input("what is your occupation?:", "alpha")
tribe = get_valid_input("what nigeria tribe are you from?:", "alpha")

print("\n--- Profile Created Successfully ---")
print(f"Name: {first_name} {last_name}")
print(f"Age:  {age}")
print(f"gender: {gender}")
print(f"state : {state}")
print(f"occupation : {occupation}")
print(f"tribe : {tribe}")