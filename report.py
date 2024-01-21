import json
import random

def generate_group_id():
    # Generate a random group identifier
    return random.randint(1, 1000)

def get_group_info():
    location = input("Enter location of the crime: ")
    activity = input("Enter type of crime: ")
    return location, activity

def get_people_descriptions(num_people):
    groups = {}

    # Get group information at the beginning
    location, activity = get_group_info()

    for i in range(1, num_people + 1):
        print(f"\nEnter description for person {i}:")
        gender = input("Gender: ")
        age = input("Age: ")
        race = input("Race: ")
        clothing = input("Clothing:")
        weapons = input("Weapons:")

        person_info = {
            "Gender": gender,
            "Race": race,
            "Age": age,
            "Clothing": clothing,
            "Weapons": weapons,
        }

        # Create a new group or add to an existing group
        if i == 1:
            group_id = generate_group_id()
            groups[group_id] = {"Location": location, "Activity": activity, "People": []}

        groups[group_id]["People"].append(person_info)

    return groups

def save_to_json(data, filename="people_groups.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=2)
    print(f"\nData saved to {filename} successfully.")

def main():
    try:
        num_people = int(input("Enter the number of people: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if num_people <= 0:
        print("Please enter a positive number of people.")
        return

    people_data = get_people_descriptions(num_people)
    save_to_json(people_data)

if __name__ == "__main__":
    main()
