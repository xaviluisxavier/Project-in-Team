class TrailManager:

# Create a Trail on the Trail File
    def createTrail(self, filename: str):
        name = input('Trail name -> ')
        island = input('Island -> ')
        council = input('Municipal Council -> ')
        coordenates_GPS = input('Coordenates GPS -> ')
        print("Degree of difficulty:")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        Degree_difficulty = input('Choose the Degree of difficulty (1/2/3) -> ')
        Degree_difficulty = ['Easy', 'Medium', 'Hard'][int(Degree_difficulty) - 1]
        print("Extension:")
        print("1. 0-5km")
        print("2. 5-10km")
        print("3. 10-15km")
        print("4. 15-30km")
        print("5. +30km")
        extension = input('Choose the extension (1/2/3/4/5) -> ')
        extension = ['0-5km', '5-10km', '10-15km', '15-30km', '+30km'][int(extension) - 1]
        print("Form:")
        print("1. Circular")
        print("2. Linear")
        form = input('Choose the format (1/2) -> ')
        form = ['Circular', 'Linear'][int(form) - 1]
        description = input('Brief description -> ')
        file = open(filename, 'a', encoding='utf-8')
        file.write('\n' + name + ';' + island + ';' + council + ';' + coordenates_GPS + ';' +
                   Degree_difficulty + ';' + extension + ';' + form + ';' + description)
        file.close()
        print(f"Trail: {name} successfully created!")
        return None
        # Removes a Trail from the Trail File
    def removeTrail(self, filename: str):
        name_trail = input('Name of the trail to be removed -> ')
        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()
        lst = []
        for line in lines:
            if not name_trail in line.split(';')[0]:
                lst.append(line)
        file.close()
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lst:
                file.write(line)
        print(f"Trail: {name_trail} successfully removed!")
        return file
        # Updates a Trail from the Trail File
    def updateTrail(self, filename: str):
        # Prompts the user for the name of the trail and the category to be updated
        name_trail = input('Name of the Trail to be updated -> ')
        category = input(
            'Category to be updated (name, island, Municipal Council, coordenates_GPS, Degree_difficulty, extension, form, description) -> ')
        new_valor = input(f'New valor {category}-> ')
        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()
        file.close()
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lines:
                if not name_trail in line.split(';')[0]:
                    file.write(line)
                else:
                    a = line.split(';')
                    if category.lower() == 'name':
                        a[0] = new_valor
                    elif category.lower() == 'island':
                        a[1] = new_valor
                    elif category.lower() == 'concil':
                        a[2] = new_valor
                    elif category.lower() == 'coordenates_GPS':
                        a[3] = new_valor
                    elif category.lower() == 'Degree_difficulty':
                        a[4] = new_valor
                    elif category.lower() == 'extension':
                        a[5] = new_valor
                    elif category.lower() == 'form':
                        a[6] = new_valor
                    elif category.lower() == 'description':
                        a[7] = new_valor
                    # Write the updated line to the file
                    file.write(';'.join(a))
                    print(f'Category: {category} | Updated Trail: {name_trail} | Update: {new_valor}')
        return None
        # Read a Trail from the Trail File
    def readTrail(self, filename: str):
        name_trail = input('Enter the trail name -> ')
        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()
        for line in lines:
            if name_trail in line.split(';')[0]:  # Checks if the trail name is in the first column
                # Using join to format output with spaces
                print("Trail informations:")
                print(" | ".join(line.split(';')))  # Use ' | ' as separator between fields
            else:
                pass
        file.close()
        return None
