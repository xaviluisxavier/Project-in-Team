class TrailManager:
        # Create a Trail on the Trail File
    def createTrail(self, filename: str):
        nome = input('Nome do trilho -> ')
        ilha = input('Ilha -> ')
        concelho = input('Concelho -> ')
        coordenadas_gps = input('Coordenadas GPS -> ')
        print("Grau de dificuldade:")
        print("1. Fácil")
        print("2. Médio")
        print("3. Difícil")
        grau_dificuldade = input('Escolha o grau de dificuldade (1/2/3) -> ')
        grau_dificuldade = ['Fácil', 'Médio', 'Difícil'][int(grau_dificuldade) - 1]
        print("Extensão:")
        print("1. 0-5km")
        print("2. 5-10km")
        print("3. 10-15km")
        print("4. 15-30km")
        print("5. +30km")
        extensao = input('Escolha a extensão (1/2/3/4/5) -> ')
        extensao = ['0-5km', '5-10km', '10-15km', '15-30km', '+30km'][int(extensao) - 1]
        print("Forma:")
        print("1. Circular")
        print("2. Linear")
        forma = input('Escolha a forma (1/2) -> ')
        forma = ['Circular', 'Linear'][int(forma) - 1]
        descricao = input('Breve descrição -> ')
        file = open(filename, 'a', encoding='utf-8')
        file.write('\n' + nome + ';' + ilha + ';' + concelho + ';' + coordenadas_gps + ';' +
                   grau_dificuldade + ';' + extensao + ';' + forma + ';' + descricao)
        file.close()
        print(f"Trilho: {nome} criado com sucesso!")
        return None
    # Removes a Trail from the Trail File
    def removeTrail(self, filename: str):
        nome_trilho = input('Nome do trilho a ser removido -> ')
        file = open(filename, 'r', encoding='utf-8')
        lines = file.readlines()
        lst = []
        for line in lines:
            if not nome_trilho in line.split(';')[0]:
                lst.append(line)
        file.close()
        with open(filename, 'w', encoding='utf-8') as file:
            for line in lst:
                file.write(line)
        print(f"Trilho: {nome_trilho} removido com sucesso!")
        return file
        # Updates a Trail from the Trail File
    def updateTrail(self, filename:str):
            # Solicita ao usuário o nome do trilho e a categoria a ser atualizada
            nome_trilho = input('Nome do trilho a ser atualizado -> ')
            categoria = input(
                'Categoria a ser atualizada (nome, ilha, concelho, coordenadas_gps, grau_dificuldade, extensao, forma, descricao) -> ')
            novo_valor = input(f'Novo valor {categoria}-> ')
            file = open(filename, 'r', encoding='utf-8')
            lines = file.readlines()
            file.close()
            with open(filename, 'w', encoding='utf-8') as file:
                for line in lines:
                    if not nome_trilho in line.split(';')[0]:
                        file.write(line)
                    else:
                        a = line.split(';')
                        if categoria.lower() == 'nome':
                            a[0] = novo_valor
                        elif categoria.lower() == 'ilha':
                            a[1] = novo_valor
                        elif categoria.lower() == 'concelho':
                            a[2] = novo_valor
                        elif categoria.lower() == 'coordenadas_gps':
                            a[3] = novo_valor
                        elif categoria.lower() == 'grau_dificuldade':
                            a[4] = novo_valor
                        elif categoria.lower() == 'extensao':
                            a[5] = novo_valor
                        elif categoria.lower() == 'forma':
                            a[6] = novo_valor
                        elif categoria.lower() == 'descricao':
                            a[7] = novo_valor
                        # Escreve a linha atualizada no arquivo
                        file.write(';'.join(a))
                        print(f'Categoria: {categoria} | atualizada no trilho: {nome_trilho} | Atualizaçao: {novo_valor}')
            return None
        # Read a Trail from the Trail File
    def readTrail(self, filename: str):
            nome_trilho = input('Insira o nome do trilho -> ')
            file = open(filename, 'r', encoding='utf-8')
            lines = file.readlines()
            for line in lines:
                if nome_trilho in line.split(';')[0]:  # Verifica se o nome do trilho está na primeira coluna
                    # Usando join para formatar a saída com espaços
                    print("Informações do trilho:")
                    print(" | ".join(line.split(';')))  # Usa ' | ' como separador entre os campos
                else:
                    pass
            file.close()
            return None