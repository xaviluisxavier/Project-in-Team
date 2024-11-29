class TrailManager:
    # Create a trail
    def createTrail(self):
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
        file = open('trails.csv', 'a', encoding='utf-8')
        file.write('\n' + nome + ';' + ilha + ';' + concelho + ';' + coordenadas_gps + ';' +
                   grau_dificuldade + ';' + extensao + ';' + forma + ';' + descricao)
        file.close()
        print("Trilho criado com sucesso!")
        return None