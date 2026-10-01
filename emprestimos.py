
def inclui_emprestimo(con, usuario, livro):

    sql_insert = "INSERT INTO emprestimos (usuario_id) VALUES ({usuario})"
    con.execute(sql_insert)
