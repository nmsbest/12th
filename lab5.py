# Function That Prefixes Based On Gender
# Credits: Dhruv , XII-D

def check_gender_give_prefix(name,gender):
    if gender.lower() == "male":
        print(f"Mr. {name}")
    else:
        print(f"Ms. {name}")

name = str(input("Name: "))
gender = str(input("Gender: "))

check_gender_give_prefix(name,gender)
