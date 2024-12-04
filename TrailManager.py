class TrailManager:
    def __init__(self):
        self._id = ""  # New attribute for the trail ID
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
        if not value:
            raise ValueError("ID cannot be empty")
        self._id = value

    def set_name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    def set_island(self, value):
        if not value:
            raise ValueError("Island cannot be empty")
        self._island = value

    def set_council(self, value):
        if not value:
            raise ValueError("Council cannot be empty")
        self._council = value

    def set_coordinates_GPS(self, value):
        if not value:
            raise ValueError("Coordinates GPS cannot be empty")
        self._coordinates_GPS = value

    def set_difficulty(self, value):
        if value not in ['Easy', 'Medium', 'Hard']:
            raise ValueError("Invalid difficulty level")
        self._difficulty = value

    def set_extension(self, value):
        valid_extensions = ['0-5km', '5-10km', '10-15km', '15-30km', '+30km']
        if value not in valid_extensions:
            raise ValueError("Invalid extension")
        self._extension = value

    def set_form(self, value):
        if value not in ['Circular', 'Linear']:
            raise ValueError("Invalid form")
        self._form = value

    def set_description(self, value):
        if not value:
            raise ValueError("Description cannot be empty")
        self._description = value

    def create_trail(self, filename: str):
        # Set the trail ID
        self.set_id(input('Trail ID -> '))  # Ask for the trail ID
        self.set_name(input('Trail name -> '))
        self.set_island(input('Island -> '))
        self.set_council(input('Municipal Council -> '))
        self.set_coordinates_GPS(input('GPS Coordinates -> '))

        print("Degree of difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")

        choice = input('Choose the Degree of difficulty (1/2/3) -> ')

        difficulties = ['Easy', 'Medium', 'Hard']

        self.set_difficulty(difficulties[int(choice) - 1])

        print("Extension:")

        print("1. 0-5km")
        print("2. 5-10km")
        print("3. 10-15km")
        print("4. 15-30km")
        print("5. +30km")

        choice = input('Choose the extension (1/2/3/4/5) -> ')

        extensions = ['0-5km', '5-10km', '10-15km', '15-30km', '+30km']

        self.set_extension(extensions[int(choice) - 1])

        print("Form:")

        print("1. Circular")
        print("2. Linear")

        choice = input('Choose the format (1/2) -> ')

        forms = ['Circular', 'Linear']

        self.set_form(forms[int(choice) - 1])

        self.set_description(input('Brief description -> '))

        # Save trail data
        with open(filename, 'a', encoding='utf-8') as file:
            trail_data = ';'.join([
                self.get_id(),  # Include ID in the saved data
                self.get_name(),
                self.get_island(),
                self.get_council(),
                self.get_coordinates_GPS(),
                self.get_difficulty(),
                self.get_extension(),
                self.get_form(),
                self.get_description()
            ])
            file.write('\n' + trail_data)

        print(f"Trail: {self.get_name()} successfully created!")

# Removes a Trail from the Trail File
    def remove_trail(self, filename: str):
        # Ask for the trail ID to be removed
        self.trail_id = input('Trail ID to be removed -> ')

        # Open the file and read lines
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        lst = []

        # Iterate through the lines to find the trail with the specified ID
        for line in lines:
            if not self.trail_id in line.split(';')[0]:  # Assuming ID is the first element
                lst.append(line)

        # Write back the remaining lines to the file
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lst:
                file.write(line)

        print(f"Trail with ID: {self.trail_id} successfully removed!")

    def update_trail(self, filename: str):
        self._id = input('ID of the Trail to be updated -> ')  # Use a local variable for ID
        category = input(
            'Category to be updated (name, island, council, coordinates_GPS, difficulty, extension, form, description) -> ')

        # Open the file and read lines
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Variable to hold updated line
        updated_line = None

        for line in lines:
            if self._id in line.split(';')[0]:  # Check if the ID matches
                a = line.split(';')

                # Retrieve current value using getter if applicable
                if category.lower() == 'name':
                    current_value = a[1]  # Assuming name is at index 1
                    new_value = input(f'Current value is "{current_value}". New value for {category} -> ')
                    self.set_name(new_value)  # Update using setter
                    a[1] = new_value  # Update list

                elif category.lower() == 'island':
                    current_value = a[2]  # Assuming island is at index 2
                    new_value = input(f'Current value is "{current_value}". New value for {category} -> ')
                    self.set_island(new_value)
                    a[2] = new_value

                elif category.lower() == 'council':
                    current_value = a[3]  # Assuming council is at index 3
                    new_value = input(f'Current value is "{current_value}". New value for {category} -> ')
                    self.set_council(new_value)
                    a[3] = new_value

                elif category.lower() == 'coordinates_gps':
                    current_value = a[4]  # Assuming coordinates_GPS is at index 4
                    new_value = input(f'Current value is "{current_value}". New value for {category} -> ')
                    self.set_coordinates_GPS(new_value)
                    a[4] = new_value

                elif category.lower() == 'difficulty':
                    current_value = a[5]  # Assuming difficulty is at index 5
                    new_value = input(f'Current value is "{current_value}". New value for {category} -> ')
                    self.set_difficulty(new_value)
                    a[5] = new_value

                elif category.lower() == 'extension':
                    current_value = a[6]  # Assuming extension is at index 6
                    new_value = input(f'Current value is "{current_value}". New value for {category} -> ')
                    self.set_extension(new_value)
                    a[6] = new_value

                elif category.lower() == 'form':
                    current_value = a[7]  # Assuming form is at index 7
                    new_value = input(f'Current value is "{current_value}". New value for {category} -> ')
                    self.set_form(new_value)
                    a[7] = new_value

                elif category.lower() == 'description':
                    current_value = a[8]  # Assuming description is at index 8
                    new_value = input(f'Current value is "{current_value}". New value for {category} -> ')
                    self.set_description(new_value)
                    a[8] = new_value

                # Create updated line from modified list
                updated_line = ';'.join(a) + '\n'
                break  # Exit loop after updating

        # Write back updated lines to the file if an update occurred
        if updated_line:
            with open(filename, 'w', encoding='utf-8') as file:
                for line in lines:
                    if self._id in line.split(';')[0]:
                        file.write(updated_line)  # Write updated line
                    else:
                        file.write(line)  # Write unchanged lines

            print(f'Trail with ID: {self._id} successfully updated!')
        else:
            print(f"No trail found with ID: {self._id}")  # Print message if no match was found


    def read_trail(self, filename: str):
        self._id = input('Enter the trail ID -> ')  # Change from name to ID

        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()

        found = False  # Flag to check if any trail is found

        for line in lines:
            if self._id in line.split(';')[0]:  # Checks if the trail ID is in the first column
                found = True
                # Assuming you have a way to set the current values based on this line
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
            print(f"No trail found with ID: {self._id}")  # Print message if no match was found
