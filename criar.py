import sys
import os
from github import Github
from dotenv import load_dotenv

# carrega o arquivo .env para que os dados contidos nele possam ser usados neste programa:
load_dotenv()

# lendo as variáveis criadas dentro do arquivo .env:
caminho = os.getenv("CAMINHO")
usuario = os.getenv("USUARIO")
senha = os.getenv("SENHA")

# função que automatiza, em CLI, o processo de criar a pasta local do projeto e o repositório remoto:
def create():
    # lembrando que sys.argv[1] é o argumento que será passado junto no chamado da função ("criar nomeProjeto"):
    nomePasta = str(sys.argv[1])
    # criando a pasta local do projeto:
    os.makedirs(caminho + str(nomePasta))
    # logando no git:
    loginUsuario = Github(usuario, senha).get_user()
    # criando repo:
    repo = loginUsuario.create_repo(nomePasta)
    print(f"Repositório {nomePasta} criado com sucesso!")

if __name__ == "__main__":
    create()
