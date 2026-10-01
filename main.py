import sqlite3 as sqlite

from util import limpa_tela

from usuarios import lista_usuarios
from usuarios import inclui_usuario

from autores import inclui_autor , lista_autores , get_id_autor

from editoras import lista_editoras , inclui_editora , get_id_editora

from livros import inclui_livro 
from livros import lista_livros

from emprestimos import inclui_emprestimo , lista_emprestimos

conn = sqlite.connect("biblioteca.db")
conn.row_factory = sqlite.Row

def menu_usuarios():

    while(True):
    
        limpa_tela()
        print("-----Menu Usuários-----")
        print("[1]-Incluir\n[2]-Listar\n[3]Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            nome = input("Nome de usuário: ")
            inclui_usuario(conn, nome)
        elif (opcao == '2'):
            lista_usuarios(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == 3):
            limpa_tela()
            break
        else:
            print("Opção inválida! Digite uma tecla para continuar...")

def menu_autores():

    while(True):
    
        limpa_tela()
        print("-----Menu Autores-----")
        print("[1]-Incluir\n[2]-Listar\n[3]Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            nome = input("Nome do Autor(a): ")
            inclui_autor(conn, nome)
        elif (opcao == '2'):
            lista_autores(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == 3):
            limpa_tela()
            break
        else:
            print("Opção inválida! Digite uma tecla para continuar...")

def menu_editoras():

    while(True):
    
        limpa_tela()
        print("-----Menu Editoras-----")
        print("[1]-Incluir\n[2]-Listar\n[3]Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            nome = input("Nome da editora): ")
            inclui_editora(conn, nome)
        elif (opcao == '2'):
            lista_editoras(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == 3):
            limpa_tela()
            break
        else:
            print("Opção inválida! Digite uma tecla para continuar...")

def menu_livros():

    while(True):
    
        limpa_tela()
        print("-----Menu Livros-----")
        print("[1]-Incluir\n[2]-Listar\n[3]Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor(a): ")
            id_autor = get_id_autor(conn, nome_autor)
            nome_editora = input("Nome da editora: ")
            id_editora = get_id_editora(conn, nome_editora)
            ano_publicacao = int(input("Ano de publicação: "))
            edicao = int(input("Ano de publicação: "))
            inclui_editora(conn, titulo)
        elif (opcao == '2'):
            lista_livros(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == 3):
            limpa_tela()
            break
        else:
            print("Opção inválida! Digite uma tecla para continuar...")

def menu_emprestimos():

    while(True):
    
        limpa_tela()
        print("-----Menu de Empréstimos-----")
        print("[1]-Incluir\n[2]-Listar\n[3]Voltar")
        opcao = input("Digite a opção: ")
        if (opcao == '1'):
            usuario = 1
            livros = []
            while(True):
                titulo_livro = input("Digite o título do livro: ")
                livros.append(titulo_livro)
                opcao = input("Digite S para incluir novo livro ou qualquer tecla para fechar a lista.")
                if (opcao.upper() != 'S'):
                    break

            inclui_emprestimo(conn, usuario, livros)

        elif (opcao == '2'):
            lista_livros(conn)
            input("Digite uma tecla para continuar...")
        elif (opcao == 3):
            limpa_tela()
            break
        else:
            print("Opção inválida! Digite uma tecla para continuar...")

while(True):
    limpa_tela()
    print("------Sistema da Biblioteca------") 
    print("Digite:\n[1]-Usuários\n[2]-Autores\n[3]-Editoras\n[4]-Livros")
    opcao = input("Digite a opção: ")

    if (opcao =='1'):
        menu_usuarios()
    elif (opcao == '2'):
        menu_autores()
    elif (opcao == '3'):
        menu_editoras()
    elif (opcao == '4'):
        menu_livros()
    elif (opcao == '5'):
        menu_emprestimos()
    else:
        break
#fecha a conexão
conn.close()

conn = sqlite.connect("biblioteca.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()

for linha in resultados:
    print(f"id: {linha[0]} | nome: {linha[1]}")

conn.close()


