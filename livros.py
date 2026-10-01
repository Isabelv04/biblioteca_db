def inclui_livro(con, titulo):
    con.execute("INSERT INTO livros(titulo) VALUES(?)",
                 (titulo,))
    con.commit()

def lista_livros(con):
    #cria um cursor (objeto para interagir com o banco)
    cursor = con.cursor()

#executa o sql
    cursor.execute("SELECT * FROM livros")

#pega os registros e guarda na variável resultados
    resultados = cursor.fetchall()

#percorre os registros que retornaram
    for linha in resultados:
        print(f"id: {linha['id']} | nome: {linha['nome']}")
    #print(f"id: {linha[0]} | nome: {linha[1]}")