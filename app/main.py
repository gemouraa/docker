from models.usuario_model import Usuario
from services.usuario_services import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session


def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)


    print("\nAdicionando usuário. ")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")

    service.criar_usuario(nome=nome, email=email, senha=senha)

    print("\nListando usuários cadastrados.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")

if __name__ == "__main__":
        main()        