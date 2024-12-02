import json

class Guia:
    @staticmethod
    def adicionar_guia(filename: str):
        """Coleta informações do guia e adiciona ao arquivo JSON."""
        # Coleta informações do usuário
        nome = input("Digite o nome do guia: ")
        experiencia = int(input("Digite a experiência (em anos): "))
        telefone = input("Digite o telefone do guia: ")
        email = input("Digite o e-mail do guia: ")
        idiomas = input("Digite os idiomas (separados por vírgula): ").split(',')
        disponibilidade = input("Digite a disponibilidade (separados por vírgula): ").split(',')
        # Criação do dicionário do novo guia
        novo_guia = {
            "nome": nome,
            "experiencia": experiencia,
            "contato": {
                "telefone": telefone,
                "email": email
            },
            "idiomas": [idioma.strip() for idioma in idiomas],
            "disponibilidade": [dia.strip() for dia in disponibilidade]
        }
        # Inicializa a lista de guias
        data = []
        # Tenta abrir o arquivo para leitura
        try:
            with open(filename, 'r') as file:
                data = json.load(file)  # Carrega a lista de guias
        except FileNotFoundError:
            # Se o arquivo não existir, continua com data como uma lista vazia
            pass
        # Adiciona o novo guia à lista
        data.append(novo_guia)
        # Salva as alterações de volta no arquivo
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print("Guia adicionado com sucesso!")