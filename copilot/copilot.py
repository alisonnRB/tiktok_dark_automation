import subprocess

class Copilot:
    name_path_copilot = "Microsoft.Copilot_8wekyb3d8bbwe!App"

    @staticmethod
    def open():
        try:
            subprocess.run(f"start shell:AppsFolder\\{Copilot.name_path_copilot}", shell=True)
            print("Copilot aberto com sucesso.")
        except Exception as e:
            print(f"Erro ao tentar abrir o Copilot: {e}")
