import os

class Prompt:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_prompt_base = os.path.join(base_dir, 'prompt_base.txt') 
    file_animals = os.path.join(base_dir, 'animal.txt')
    file_index = os.path.join(base_dir, 'index.txt')

    def __init__(self):
        self.prompt_base = self.converter__para_string_prompt_base()
        self.animals = self.converter_para_lista_profissoes()
        self.index = self.index_current()
        self.prompt = self.prompt_base + "Hoje eu quero reproduzir um video detalhado de uma criatura colossal nunca antes avistada no oceano e sendo vista por cientistas. O ambiente deve ser sombrio e a criatura baseada em um " + self.animals[self.index] + ".  A criatura deve ser muito grande, com características únicas e assustadoras. A descrição deve ser curta, mas imersiva, focando na atmosfera de mistério e terror das profundezas."

    def converter__para_string_prompt_base(self):
        try:
            with open(self.file_prompt_base, 'r', encoding='utf-8') as file:
                content = file.read() 
            return content
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return None

    def converter_para_lista_profissoes(self):
        try:
            with open(self.file_animals, 'r', encoding='utf-8') as file:
                profissoes = [linha.strip() for linha in file.readlines()]
            return profissoes
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return []
        
    def index_save(self):
        try:
            with open(self.file_index, 'w', encoding='utf-8') as file:
                file.write(str(self.index + 1))
            print(f"Conteúdo do arquivo '{self.file_index}' apagado e novo conteúdo escrito com sucesso.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

    def index_current(self):
        try:
            with open(self.file_index, 'r', encoding='utf-8') as file:
                content = file.read() 
                if content == "":
                    return 0
                else:
                    return int(content)
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")
            return None