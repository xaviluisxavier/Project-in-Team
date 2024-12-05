class TrailManager:
    def __init__(self):
        self.trail_id = ""
        self._id = ""
        self._name = ""
        self._island = ""
        self._council = ""
        self._coordinates_GPS = ""
        self._difficulty = ""
        self._extension = ""
        self._form = ""
        self._description = ""
    # Getter methods
    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_island(self):
        return self._island

    def get_council(self):
        return self._council

    def get_coordinates_GPS(self):
        return self._coordinates_GPS

    def get_difficulty(self):
        return self._difficulty

    def get_extension(self):
        return self._extension

    def get_form(self):
        return self._form

    def get_description(self):
        return self._description

    # Setter methods
    def set_id(self, value):
        if value:
            self._id = value
    def set_name(self, value):
        if value:
            self._name = value
    def set_island(self, value):
        if value:
            self._island = value

    def set_council(self, value):
        if value:
            self._council = value

    def set_coordinates_GPS(self, value):
        if value:
            self._coordinates_GPS = value

    def set_difficulty(self, value):
        if value  in ['Easy', 'Medium', 'Hard']:
            self._difficulty = value

    def set_extension(self, value):
        valid_extensions = ['0-5km', '5-10km', '10-15km', '15-30km', '+30km']
        if value in valid_extensions:
            self._extension = value

    def set_form(self, value):
        if value in ['Circular', 'Linear']:
            self._form = value

    def set_description(self, value):
        if value:
            self._description = value

    def create_trail(self, filename: str):
        print("\n--- Create New Trail ---")
        while True:
                # Set the trail ID
                id = input('Trail ID (or "exit" to terminate) -> ').strip()
                if id.lower() == 'exit':
                    return
                while not id:
                    id = input('ID cannot be empty. Trail ID -> ').strip()
                self.set_id(id)

                # Set other attributes
                name = input('Trail name -> ').strip()
                while not name:
                    name = input('Name cannot be empty. Trail name -> ').strip()
                self.set_name(name)

                island = input('Island -> ').strip()
                while not island:
                    island = input('Island cannot be empty. Island -> ').strip()
                self.set_island(island)

                council = input('Municipal Council -> ').strip()
                while not council:
                    council = input('Council cannot be empty. Municipal Council -> ').strip()
                self.set_council(council)

                coordinates = input('GPS Coordinates -> ').strip()
                while not coordinates:
                    coordinates = input('GPS Coordinates cannot be empty. GPS Coordinates -> ').strip()
                self.set_coordinates_GPS(coordinates)

                # Difficulty
                print("Degree of difficulty: 1. Easy, 2. Medium, 3. Hard")
                choice = input('Choose the Degree of difficulty (1/2/3) -> ').strip()
                while choice not in ['1', '2', '3']:
                    choice = input('Invalid choice. Choose the Degree of difficulty (1/2/3) -> ').strip()
                difficulties = ['Easy', 'Medium', 'Hard']
                self.set_difficulty(difficulties[int(choice) - 1])

                # Extension
                print("Extension: 1. 0-5km, 2. 5-10km, 3. 10-15km, 4. 15-30km, 5. +30km")
                choice = input('Choose the extension (1/2/3/4/5) -> ').strip()
                while choice not in ['1', '2', '3', '4', '5']:
                    choice = input('Invalid choice. Choose the extension (1/2/3/4/5) -> ').strip()
                extensions = ['0-5km', '5-10km', '10-15km', '15-30km', '+30km']
                self.set_extension(extensions[int(choice) - 1])

                # Form
                print("Form: 1. Circular, 2. Linear")
                choice = input('Choose the format (1/2) -> ').strip()
                while choice not in ['1', '2']:
                    choice = input('Invalid choice. Choose the format (1/2) -> ').strip()
                forms = ['Circular', 'Linear']
                self.set_form(forms[int(choice) - 1])

                # Description
                description = input('Brief description -> ').strip()
                while not description:
                    description = input('Description cannot be empty. Brief description -> ').strip()
                self.set_description(description)

                # Save trail data
                with open(filename, 'a', encoding='utf-8') as file:
                    trail_data = ';'.join([
                        self.get_id(),
                        self.get_name(),
                        self.get_island(),
                        self.get_council(),
                        self.get_coordinates_GPS(),
                        self.get_difficulty(),
                        self.get_extension(),
                        self.get_form(),
                        self.get_description()
                    ])
                    file.write(trail_data + '\n')
                print(f"Trail: {self.get_name()} successfully created!")
    print("Trail creation process finished.")

    # Removes a Trail from the Trail File
    def remove_trail(self, filename: str):
        while True:
                # Ask for the trail ID to be removed
                trail_id = input('Trail ID to be removed (or "exit" to cancel) -> ').strip()
                if trail_id.lower() == 'exit':
                    print("Trail removal cancelled.")
                    return
                if not trail_id:
                    print("Trail ID cannot be empty. Please try again.")
                    continue
                # Open the file and read lines
                with open(filename, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                trail_found = False
                updated_lines = []
                # Iterate through the lines to find the trail with the specified ID
                for line in lines:
                    if trail_id == line.split(';')[0]:
                        trail_found = True
                    else:
                        updated_lines.append(line)
                if not trail_found:
                    print(f"No trail found with ID: {trail_id}. Please try again.")
                    continue
                # Write back the remaining lines to the file
                with open(filename, 'w', encoding='utf-8') as file:
                    file.writelines(updated_lines)
                print(f"Trail with ID: {trail_id} successfully removed!")
                break
        print("Trail removal process finished.")

    # Update a category Trail from the Trail File
    def update_trail(self, filename: str):
        while True:  # Loop to allow multiple attempts
            self._id = input('ID of the Trail to be updated (or "exit" to cancel) -> ').strip()
            if self._id.lower() == 'exit':
                print("Update cancelled.")
                return
            if not self._id:
                print("Trail ID cannot be empty. Please try again.")
                continue  # Continue the loop for valid ID input
            # Open the file and read lines
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            # Check if the ID exists in the file
            id_found = False  # Flag to check if ID was found
            for line in lines:
                if self._id in line.split(';')[0]:  # Check if the ID matches
                    id_found = True  # Set flag to true if ID is found
                    break  # Exit loop if ID is found
            if not id_found:  # Check if the ID was found after the loop
                print(f"No trail found with ID: {self._id}. Please try again.")
                continue  # Continue the loop to allow another attempt
            while True:  # Loop for category input
                category = input(
                    'Category to be updated (name, island, council, coordinates_GPS, difficulty, extension, form, description) -> ').strip().lower()
                # Validate category
                valid_categories = ['name', 'island', 'council', 'coordinates_gps', 'difficulty', 'extension', 'form',
                                    'description']
                if category in valid_categories:
                    break  # Exit loop if valid category is provided
                else:
                    print(f"Invalid category. Please choose from: {', '.join(valid_categories)}")
            # Variable to hold updated line
            updated_line = None
            for line in lines:
                if self._id in line.split(';')[0]:  # Check if the ID matches
                    a = line.strip().split(';')
                    while True:  # Loop for new value input based on category
                        current_value = a[
                            valid_categories.index(category) + 1]  # Get current value based on category index
                        new_value = input(
                            f'Current value is "{current_value}". New value for {category} -> ').strip()
                        if not new_value:
                            print(f"{category.capitalize()} cannot be empty. Please enter a valid value.")
                            continue  # Continue prompting for a new value
                        # Update using setter based on category
                        if category == 'name':
                            self.set_name(new_value)
                            a[1] = new_value
                        elif category == 'island':
                            self.set_island(new_value)
                            a[2] = new_value
                        elif category == 'council':
                            self.set_council(new_value)
                            a[3] = new_value
                        elif category == 'coordinates_gps':
                            self.set_coordinates_GPS(new_value)
                            a[4] = new_value
                        elif category == 'difficulty':
                            self.set_difficulty(new_value)
                            a[5] = new_value
                        elif category == 'extension':
                            self.set_extension(new_value)
                            a[6] = new_value
                        elif category == 'form':
                            self.set_form(new_value)
                            a[7] = new_value
                        elif category == 'description':
                            self.set_description(new_value)
                            a[8] = new_value
                        # Create updated line from modified list
                        updated_line = ';'.join(a) + '\n'
                        break  # Exit loop after updating
                    break  # Exit outer loop after finding and updating
            # Write back updated lines to the file if an update occurred
            if updated_line:
                with open(filename, 'w', encoding='utf-8') as file:
                    for line in lines:
                        file.write(updated_line if self._id in line.split(';')[0] else line)
                print(f'Trail with ID: {self._id} successfully updated!')
                return  # Exit the method after successful update
        print("Update process finished.")  # Final message after exiting the loop

    #read a trail in the trail file
    def read_trail(self, filename: str):
        self._id = input('Enter the trail ID -> ')  # Change from name to ID
        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()
        found = False  # Flag to check if any trail is found
        for line in lines:
            if self._id in line.split(';')[0]:  # Checks if the trail ID is in the first column
                found = True
                a = line.split(';')
                self.set_id(a[0])
                self.set_name(a[1])
                self.set_island(a[2])
                self.set_council(a[3])
                self.set_coordinates_GPS(a[4])
                self.set_difficulty(a[5])
                self.set_extension(a[6])
                self.set_form(a[7])
                self.set_description(a[8])
                print("Trail informations:")
                print(" | ".join(line.split(';')))  # Use ' | ' as separator between fields
        file.close()
        if not found:
            print(f"No trail found with ID: {self._id}")
