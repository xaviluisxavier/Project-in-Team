import json
class GuideManager:
    def __init__(self, name: str, experience: int, number: str, email: str, languages: list, availability: list):
        self._name = name
        self._experience = experience
        self._number = number
        self._email = email
        self._languages = languages
        self._availability = availability

    # Getters
    def get_name(self):
        return self._name

    def get_experience(self):
        return self._experience

    def get_number(self):
        return self._number

    def get_email(self):
        return self._email

    def get_languages(self):
        return self._languages

    def get_availability(self):
        return self._availability

    # Setters
    def set_name(self, value):
        self._name = value

    def set_experience(self, value):
        if value >= 0:
            self._experience = value
        else:
            raise ValueError("Experience must be a non-negative integer.")

    def set_number(self, value):
        self._number = value

    def set_email(self, value):
        self._email = value

    def set_languages(self, value):
        self._languages = value

    def set_availability(self, value):
        self._availability = value


    def add_guide(self,filename: str):
        # Collects information from the guide and adds it to the JSON file.

        name = input("Enter guide's name: ")
        experience = int(input("Enter experience (in years): "))
        number = input("Enter the guide's phone number: ")
        email = input("Enter the guide's email: ")

        languages_input = input("Enter languages (separated by ,): ")
        languages = [lang.strip() for lang in languages_input.split(',')]

        availability_input = input("Enter availability (separated by ,): ")
        availability = [day.strip() for day in availability_input.split(',')]

        # Create a new Guide instance
        new_guide = GuideManager(name, experience, number, email, languages, availability)
        # Load existing guides from the file or initialize an empty list if the file doesn't exist.
        try:
            with open(filename, 'r') as file:
                guides_data = json.load(file)  # Load the list of guides
        except FileNotFoundError:
            guides_data = []  # Initialize an empty list if the file does not exist

        # Add the new guide to the list
        guides_data.append({
            "name": new_guide.get_name(),
            "experience": new_guide.get_experience(),
            "number": {
                "number": new_guide.get_number(),
                "email": new_guide.get_email()
            },
            "languages": new_guide.get_languages(),
            "availability": new_guide.get_availability()
        })

        # Save changes back to the file
        with open(filename, 'w') as file:
            json.dump(guides_data, file, indent=4)

        print("Guide added successfully!")