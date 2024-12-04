import json
class Guide:
    @staticmethod
    def add_guide(filename: str):
        # Collects information from the guide and adds it to the JSON file.
        # Collects user information
        name = input("Enter guide's name: ")
        experience = int(input("Enter experience (in years): "))
        number = input("Enter the guide's phone number: ")
        email = input("Enter the guide's email: ")
        languages = input("Enter languages (separated by ,): ").split(',')
        availability = input("Enter availability (seperated by ,): ").split(',')
        # Creation of the new guide dictionary
        new_guide = {
            "name": name,
            "experience": experience,
            "number": {
                "number": number,
                "email": email
            },
            "languages": [languages.strip() for languages in languages],
            "availability": [day.strip() for day in availability]
        }
        # Initializes the tab list
        date = []
        # Try opening the file for reading
        try:
            with open(filename, 'r') as file:
                date = json.load(file)  # Load the list of guides
        except FileNotFoundError:
            # If the file does not exist, it continues with data as an empty list
            pass
        # Add the new guide to the list
        date.append(new_guide)
        # Saves changes back to the file
        with open(filename, 'w') as file:
            json.dump(date, file, indent=4)
        print("Guide added successfully!")