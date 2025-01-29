import os
from window.window import Window


class ChatGPT:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_prompt_base = os.path.join(base_dir, 'prompt_base.txt') 
    file_profissoes = os.path.join(base_dir, 'profissoes.txt')
    file_index = os.path.join(base_dir, 'index.txt')

    url = "https://chatgpt.com"

    def __init__(self):
        self.prompt_base = self.converter__para_string_prompt_base()
        self.profissoes = self.converter_para_lista_profissoes()
        self.index = self.index_current()
        self.prompt = self.prompt_base + " Hoje eu quero reproduzir uma imagem de um gatinho muito fofo trabalhando, ele etá trabalhando como " + self.profissoes[self.index]
        Window(self.url, self.prompt)

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
            with open(self.file_profissoes, 'r', encoding='utf-8') as file:
                profissoes = [linha.strip() for linha in file.readlines()]
            return profissoes
        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")
            return []
        
    def index_save(self):
        try:
            with open(self.file_index, 'w', encoding='utf-8') as file:
                file.write(str(self.index))
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
        
